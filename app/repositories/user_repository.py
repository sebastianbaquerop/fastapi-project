from typing import Optional, List
from sqlalchemy.orm import Session
from app.schemas.user_dto import UserCreateDTO, UserPatchDTO
from app.db.models.users import Users
from datetime import datetime, timezone

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, user_data: UserCreateDTO) -> Users:
        user = Users(**user_data.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def list(self) -> List[Users]:
        return self.db.query(Users).all()


    def get_by_email(self, email: str) -> Optional[Users]:
        return self.db.query(Users).filter(Users.email == email).first()
    
    def get_by_id(self, user_id: str) -> Optional[Users]:
        return self.db.query(Users).filter(Users.id == user_id).first()
    
    def update(self, user_id: int, user_data: UserCreateDTO) -> Optional[Users]:
        user = self.get_by_id(user_id)
        if not user:
            return None
        update_data = user_data.model_dump(exclude_unset=True)
        for key,value in update_data.items():
            setattr(user, key,value)
        user.updated_at = datetime.now(timezone.utc)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def patch(self, user_id: int, user_data: UserPatchDTO) -> Optional[Users]:
        user = self.get_by_id(user_id)
        if not user:
            return None
        patch_data = user_data.model_dump(exclude_unset=True)
        for key,value in patch_data.items():

                setattr(user, key,value)
        user.updated_at = datetime.now(timezone.utc)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True





