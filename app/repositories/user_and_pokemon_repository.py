from typing import Optional, List
from sqlalchemy.orm import Session
from app.schemas.user_and_pokemon_dto import UserAndPokemonsCreateDTO, UserAndPokemonsPatchDTO
from app.db.models.users_and_pokemons import UsersAndPokemons
from datetime import datetime, timezone

class UserAndPokemonRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, user_data: UserAndPokemonsCreateDTO) -> UsersAndPokemons:
        user = UsersAndPokemons(**user_data.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def list(self) -> List[UsersAndPokemons]:
        return self.db.query(UsersAndPokemons).all()


    def get_by_email(self, email: str) -> Optional[UsersAndPokemons]:
        return self.db.query(UsersAndPokemons).filter(UsersAndPokemons.email == email).first()
    
    def get_by_id(self, user_id: str) -> Optional[UsersAndPokemons]:
        return self.db.query(UsersAndPokemons).filter(UsersAndPokemons.id == user_id).first()
    
    def update(self, user_id: int, user_data: UserAndPokemonsCreateDTO) -> Optional[UsersAndPokemons]:
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
    
    def patch(self, user_id: int, user_data: UserAndPokemonsPatchDTO) -> Optional[UsersAndPokemons]:
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





