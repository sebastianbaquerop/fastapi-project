from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user_and_pokemon_dto import UsersAndPokemonsResponseList, UserAndPokemonsCreateDTO, UserAndPokemonsUpdateDTO, UserAndPokemonsPatchDTO, UsersAndPokemonsResponse, UserAndPokemonsInfoResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from starlette import status
from app.services.user_and_pokemon_service import UserAndPokemonService
from app.core.dependencies import get_http_client

router = APIRouter(tags=["Users"])

@router.get("/users/", summary="Get all users", response_model=UsersAndPokemonsResponseList, status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
async def get_users(db: Session = Depends(get_db), client = Depends(get_http_client)):

    user_service = UserAndPokemonService(db_session=db, http_client=client)
    try:
        users = user_service.get_users()
        return UsersAndPokemonsResponseList(
            code=status.HTTP_200_OK,
            message="Data obtained",
            data=users
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/users/{id}", summary="Get user info by id", response_model=UserAndPokemonsInfoResponse, status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
async def get_users_by_id(id: int, db: Session = Depends(get_db), client = Depends(get_http_client)):
    """Get user info"""
    user_service = UserAndPokemonService(db_session=db, http_client=client)

    try:
        user = await user_service.get_user_by_id(id)
        response = UserAndPokemonsInfoResponse(
            code=status.HTTP_200_OK, 
            message="Data obtained", 
            data=user)
        return response

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.post("/users", summary="Create user", response_model=UsersAndPokemonsResponse,status_code=status.HTTP_201_CREATED,dependencies=[Depends(get_db)])
async def add_user(user_data: UserAndPokemonsCreateDTO,
                   db: Session = Depends(get_db),  client = Depends(get_http_client)):
    """Create a new user."""
    user_service = UserAndPokemonService(db_session=db, http_client=client)
    try:
        user = user_service.create_user(user_data)
        response = UsersAndPokemonsResponse(
            code=status.HTTP_201_CREATED, 
            message="User created", 
            data=user)
        return response

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/users/{id}", summary="Update user by id", response_model=UsersAndPokemonsResponse, status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
async def update_user(id: int, user: UserAndPokemonsUpdateDTO, db: Session = Depends(get_db),  client = Depends(get_http_client)):
    user_service = UserAndPokemonService(db_session=db, http_client=client)
    try:
        user = user_service.update_user(id, user)
        response = UsersAndPokemonsResponse(
            code=status.HTTP_200_OK, 
            message="User info updated", 
            data=user)
        return response
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=str(e)
        )

@router.patch("/users/{id}", summary="Update some user info", response_model=UsersAndPokemonsResponse,status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,dependencies=[Depends(get_db)])
async def update_user(id: int, user_data: UserAndPokemonsPatchDTO, db: Session = Depends(get_db),  client = Depends(get_http_client)):
    user_service = UserAndPokemonService(db,client)
    try:
        user = user_service.patch_user(id, user_data)
        response = UsersAndPokemonsResponse(
            code=status.HTTP_200_OK, 
            message="User info updated", 
            data=user)
        return response
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=str(e)
        )

@router.delete("/users/{id}", summary="Delete user by id", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
async def delete_user(id: int, db: Session = Depends(get_db),  client = Depends(get_http_client)):
    """Delete user"""
    user_service = UserAndPokemonService(db_session=db, http_client=client)
    try: 
        response = {}
        user = user_service.delete_user(id)
        if not user:
            raise ValueError("The user was not deleted")
        response = {"code": 200, "message": "User deleted successfully"}
        return response
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=str(e)
        )