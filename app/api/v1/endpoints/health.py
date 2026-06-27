from fastapi import  APIRouter, Depends, status,HTTPException
from app.db.database import get_db, init_db
from sqlalchemy import text, inspect
from sqlalchemy.orm import Session

router = APIRouter(tags=["Health"])

@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check(db: Session = Depends(get_db)):
    try:
        response = {}
        stmt = text('Select 1')
        db_state = db.execute(stmt)
        if db_state:
            response["health"] = "healthy"
        # Get the connection from the session
        connection = db.connection()
        # Create inspector and check
        inspector = inspect(connection)
        if not inspector.has_table("users"):
            init_db()
            print('tables were created in the database')
            response["schemas"] = "Tables schemas were created in the database"
        response["schemas"] = "Tables are already presented in the database"
        print(f"health_check - response: {response}")

    except Exception as e:
        db = f"unhealthy: {str(e)}"
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail=db) 
        
    return {
        "code": status.HTTP_200_OK,
        "info": response
    }
