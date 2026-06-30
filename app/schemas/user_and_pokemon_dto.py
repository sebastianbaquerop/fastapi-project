from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from datetime import datetime, timezone
from app.schemas.pokemon_dto import PokemonsDTO

class UsersAndPokemonsDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    hashed_password: str
    pokemon_ids: list[int]
    created_at: Optional[datetime]  = datetime.now((timezone.utc))
    updated_at: Optional[datetime]  = datetime.now((timezone.utc))
   
    model_config = ConfigDict(from_attributes=True)  # Enable reading objects from SQLAlchemy ORM

class UserAndPokemonsDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    hashed_password: str
    pokemon_ids: list[int]
    pokemons: List[PokemonsDTO]
    created_at: Optional[datetime]  = datetime.now((timezone.utc))
    updated_at: Optional[datetime]  = datetime.now((timezone.utc))
   
    model_config = ConfigDict(from_attributes=True)  # Enable reading objects from SQLAlchemy ORM


class UserAndPokemonsCreateDTO(BaseModel):
    name: str
    email: EmailStr
    role: str
    hashed_password: str
    pokemon_ids: list[int]
    created_at: Optional[datetime]  = datetime.now((timezone.utc))
    updated_at: Optional[datetime]  = datetime.now((timezone.utc))

    model_config = ConfigDict(from_attributes=True) # Enable reading objects from SQLAlchemy ORM

class UserAndPokemonsUpdateDTO(BaseModel):
    name: str
    email: EmailStr
    role: str
    hashed_password: str
    pokemon_ids: list[int]
    created_at: Optional[datetime]  = datetime.now((timezone.utc))
    updated_at: Optional[datetime]  = datetime.now((timezone.utc))

class UserAndPokemonsPatchDTO(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    hashed_password: Optional[str] = None
    pokemon_ids: Optional[list[int]] = None
    created_at: Optional[datetime]  = datetime.now((timezone.utc))
    updated_at: Optional[datetime]  = datetime.now((timezone.utc))

class UsersAndPokemonsResponse(BaseModel):
    code: int
    message: str
    data: UsersAndPokemonsDTO

class UserAndPokemonsInfoResponse(BaseModel):
    code: int
    message: str
    data: UserAndPokemonsDTO

class UsersAndPokemonsResponseList(BaseModel):
    code: int
    message: str
    data: List[UsersAndPokemonsDTO] = []

 
    
