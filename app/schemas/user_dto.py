from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime, timezone


class UserDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    hashed_password: str
    created_at: Optional[datetime] = datetime.now(timezone.utc)
    updated_at: Optional[datetime] = datetime.now(timezone.utc)

    model_config = ConfigDict(
        from_attributes=True
    )  # Enable reading objects from SQLAlchemy ORM


class UserCreateDTO(BaseModel):
    name: str
    email: EmailStr
    role: str
    hashed_password: str
    created_at: Optional[datetime] = datetime.now(timezone.utc)
    updated_at: Optional[datetime] = datetime.now(timezone.utc)

    model_config = ConfigDict(
        from_attributes=True
    )  # Enable reading objects from SQLAlchemy ORM


class UserUpdateDTO(BaseModel):
    name: str
    email: EmailStr
    role: str
    hashed_password: str
    created_at: Optional[datetime] = datetime.now(timezone.utc)
    updated_at: Optional[datetime] = datetime.now(timezone.utc)


class UserPatchDTO(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    hashed_password: Optional[str] = None
    created_at: Optional[datetime] = datetime.now(timezone.utc)
    updated_at: Optional[datetime] = datetime.now(timezone.utc)


class UserResponse(BaseModel):
    code: int
    message: str
    data: UserDTO


class UsersResponse(BaseModel):
    code: int
    message: str
    data: List[UserDTO] = []
