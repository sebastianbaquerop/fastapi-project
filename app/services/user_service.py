from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user_dto import UserCreateDTO, UserDTO, UserPatchDTO
from typing import Optional, List
class UserService:

    def __init__(self, db_session: Session):
        self.repository = UserRepository(db_session)
        self.pokemon_api_url = "https://pokeapi.co/api/v2/pokemon/"
    
    def create_user(self, user_data: UserCreateDTO) -> UserDTO:
        user = self.repository.get_by_email(user_data.email)
        if user:
            raise ValueError("Email already registered")
        user = self.repository.create(user_data)
        user_dto = UserDTO.model_validate(user)
        return user_dto

    def get_users(self)->List[UserDTO]:
        users = self.repository.list()
        user_dto_list = [UserDTO.model_validate(user) for user in users]
        return user_dto_list
    
    def get_user_by_id(self, user_id: int) -> Optional[UserDTO]:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise ValueError("There was an error")
        user_dto = UserDTO.model_validate(user)
        return user_dto
    
    def update_user(self, user_id: int, user_data: UserCreateDTO) -> Optional[UserDTO]:
         user = self.repository.update(user_id, user_data)
         if not user:
             raise ValueError("There was an error")
         user_dto = UserDTO.model_validate(user)
         return user_dto
    
    def patch_user(self, user_id: int, user_data: UserPatchDTO) -> Optional[UserDTO]:
         user = self.repository.patch(user_id, user_data)
         if not user:
             raise ValueError("There was an error")
         user_dto = UserDTO.model_validate(user)
         return user_dto
    
    def delete_user(self, user_id: int) -> bool:
        user = self.repository.delete(user_id)
        if not user:
            raise ValueError("There was an error")
        return user
