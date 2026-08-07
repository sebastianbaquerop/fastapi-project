import pytest
from app.schemas.user_dto import UserDTO, UsersResponse, UserResponse,UserCreateDTO,UserUpdateDTO,UserPatchDTO
from typing import List

# ----- GET -----
# Response by all:
# Base: users_dto_mock
@pytest.fixture
def users_dto_mock():
    return UserDTO(
    id=1,
    name="string",
    email="user1@example.com", 
    role="string1",
    hashed_password="string1",
    created_at="2026-07-14T03:49:56.070905",
    updated_at="2026-07-14T03:49:56.070905"
    )
# Response consolidated
@pytest.fixture
def get_all_users_response_success_mock(users_dto_mock: UserDTO):
    data: List[UserDTO] = []
    data.append(users_dto_mock)

    return UsersResponse(
        code=200,
        message="Data obtained",
        data=data
    )
# Response by Id:
# Base:
@pytest.fixture
def user_dto_mock():
    return UserDTO(
        id=1, 
        name="string",
        email="user1@example.com",
        role="string1",
        hashed_password="string1",
        created_at="2026-07-14T03:49:56.070905",
        updated_at="2026-07-14T03:49:56.070905"
    )
# Response consolidated
@pytest.fixture
def get_user_info_by_id_response_success_mock(user_dto_mock: UserDTO):
    return UserResponse(
        code=200,
        message="Data obtained",
        data=user_dto_mock
    )

# ----- POST -----
# Payload:
@pytest.fixture
def user_create_dto_mock():
    return UserCreateDTO(
        name="string",
        email="user1@example.com", 
        role="string1",
        hashed_password="string1",
        created_at="2026-07-14T03:49:56.070905",
        updated_at="2026-07-14T03:49:56.070905"
    )
# Response:
@pytest.fixture
def post_users_response_success_mock(users_dto_mock: UserDTO):
    return UserResponse(
        code=201,
        message="User created",
        data=users_dto_mock
    )
@pytest.fixture
def post_error():
    return {'detail': 'Email already registered'}

# ----- PUT -----
# Payload:
@pytest.fixture
def user_update_dto_mock():
   return UserUpdateDTO(
       name="string",
       email="user@example.com",
       role="string",
       hashed_password="string",
       created_at="2026-07-14T03:49:56.070905"
   )
# Response:
@pytest.fixture
def put_users_response_success_mock(users_put_dto_mock: UserDTO):
    return UserResponse(
        code=200,
        message="User info updated",
        data=users_put_dto_mock
    )

@pytest.fixture
def users_put_dto_mock():
    return UserDTO(
    id=1,
    name="string",
    email="user@example.com",
    role="string",
    hashed_password="string",
    created_at="2026-07-14T03:49:56.070905",
    updated_at="2026-07-14T03:49:56.070905"
    )

# ----- PATCH -----
# Payload:
@pytest.fixture
def patch_user_patch_dto_mock():
   return UserPatchDTO(
       name="string3", 
       email="user2@example.com",
       role="user",
       hashed_password="string1",
       created_at="2026-07-14T03:49:56.070905",
       updated_at="2026-07-14T03:49:56.070905"
   )

# Response:
@pytest.fixture
def patch_users_response_success_mock(users_patch_dto_mock: UserDTO):
    return UserResponse(
        code=200,
        message="User info updated",
        data=users_patch_dto_mock
    )

@pytest.fixture
def users_patch_dto_mock():
    return UserDTO(
    id=1,
    name="string3",
    email="user2@example.com", 
    role="user",
    hashed_password="string1",
    created_at="2026-07-14T03:49:56.070905",
    updated_at="2026-07-14T03:49:56.070905"
    )

# ----- DELETE -----
@pytest.fixture
def delete_success():
    return {"code": 200, 
            "message": "User deleted successfully"}

# ----- GENERAL -----
@pytest.fixture
def general_error():
    return {'detail': 'There was an error'}

@pytest.fixture
def general_internal_server_error():
    return {'detail': 'Internal server error'}

