import pytest
from app.schemas.user_and_pokemon_dto import (
    UsersAndPokemonsDTO,
    UserAndPokemonsDTO,
    UserAndPokemonsCreateDTO,
    UserAndPokemonsUpdateDTO,
    UserAndPokemonsPatchDTO,
    UsersAndPokemonsResponse,
    UserAndPokemonsInfoResponse,
    UsersAndPokemonsResponseList,
)
from typing import List
from app.schemas.pokemon_dto import PokemonsDTO

# ----- GET -----
# Response by all:
# Base: users_and_pokemon_dto_mock
@pytest.fixture
def users_and_pokemon_dto_mock():
    return UsersAndPokemonsDTO(
        id=1,
        name="string",
        email="user1@example.com",
        role="string1",
        hashed_password="string1",
        pokemon_ids=[7, 8, 9],
        created_at="2026-07-14T03:49:56.070905",
        updated_at="2026-07-14T03:49:56.070905",
    )

# Response consolidated
@pytest.fixture
def get_all_users_and_pokemons_response_success_mock(
    users_and_pokemon_dto_mock: UsersAndPokemonsDTO,
):
    data: List[UsersAndPokemonsDTO] = []
    data.append(users_and_pokemon_dto_mock)

    return UsersAndPokemonsResponseList(code=200, message="Data obtained", data=data)

# Response by Id:
# Base:
@pytest.fixture
def pokemon_dto_mock_factory():
    def _pokemon_dto_mock(id: int, name: str):
        return PokemonsDTO(id=id, name=name)

    return _pokemon_dto_mock

@pytest.fixture
def user_and_pokemon_dto_mock(pokemon_dto_mock_factory):
    pokemons: List[PokemonsDTO] = [
        pokemon_dto_mock_factory(7, "squirtle"),
        pokemon_dto_mock_factory(8, "wartortle"),
        pokemon_dto_mock_factory(9, "blastoise"),
    ]
    return UserAndPokemonsDTO(
        id=1,
        name="string",
        email="user1@example.com",
        role="string1",
        hashed_password="string1",
        pokemon_ids=[7, 8, 9],
        pokemons=pokemons,
        created_at="2026-07-14T03:49:56.070905",
        updated_at="2026-07-14T03:49:56.070905",
    )

# Response consolidated
@pytest.fixture
def get_user_and_pokemons_info_by_id_response_success_mock(
    user_and_pokemon_dto_mock: UserAndPokemonsDTO,
):
    return UserAndPokemonsInfoResponse(
        code=200, message="Data obtained", data=user_and_pokemon_dto_mock
    )

# ----- POST -----
# Payload:
@pytest.fixture
def user_and_pokemons_create_dto_mock():
    return UserAndPokemonsCreateDTO(
        name="string",
        email="user1@example.com",
        role="string1",
        hashed_password="string1",
        pokemon_ids=[7, 8, 9],
        created_at="2026-07-14T03:49:56.070905",
        updated_at="2026-07-14T03:49:56.070905",
    )

# Response:
@pytest.fixture
def post_users_and_pokemons_response_success_mock(
    users_and_pokemon_dto_mock: UsersAndPokemonsDTO,
):
    return UsersAndPokemonsResponse(
        code=201, message="User created", data=users_and_pokemon_dto_mock
    )

@pytest.fixture
def post_error():
    return {"detail": "Email already registered"}

# ----- PUT -----
# Payload:
@pytest.fixture
def user_and_pokemons_update_dto_mock():
    return UserAndPokemonsUpdateDTO(
        name="string",
        email="user@example.com",
        role="string",
        hashed_password="string",
        pokemon_ids=[4, 5, 6],
        created_at="2026-07-14T03:49:56.070905",
    )

# Response:
@pytest.fixture
def put_users_and_pokemons_response_success_mock(
    put_users_and_pokemon_dto_mock: UsersAndPokemonsDTO,
):
    return UsersAndPokemonsResponse(
        code=200, message="User info updated", data=put_users_and_pokemon_dto_mock
    )

@pytest.fixture
def put_users_and_pokemon_dto_mock():
    return UsersAndPokemonsDTO(
        id=1,
        name="string",
        email="user@example.com",
        role="string",
        hashed_password="string",
        pokemon_ids=[4, 5, 6],
        created_at="2026-07-14T03:49:56.070905",
        updated_at="2026-07-14T03:49:56.070905",
    )

# ----- PATCH -----
# Payload:
@pytest.fixture
def patch_user_and_pokemons_patch_dto_mock():
    return UserAndPokemonsPatchDTO(
        name="string3",
        email="user2@example.com",
        role="user",
        hashed_password="string1",
        pokemon_ids=[7, 8, 9],
        created_at="2026-07-14T03:49:56.070905",
        updated_at="2026-07-14T03:49:56.070905",
    )

# Response:
@pytest.fixture
def patch_users_and_pokemons_response_success_mock(
    patch_users_and_pokemon_dto_mock: UsersAndPokemonsDTO,
):
    return UsersAndPokemonsResponse(
        code=200, message="User info updated", data=patch_users_and_pokemon_dto_mock
    )

@pytest.fixture
def patch_users_and_pokemon_dto_mock():
    return UsersAndPokemonsDTO(
        id=1,
        name="string3",
        email="user2@example.com",
        role="user",
        hashed_password="string1",
        pokemon_ids=[7, 8, 9],
        created_at="2026-07-14T03:49:56.070905",
        updated_at="2026-07-14T03:49:56.070905",
    )

# ----- DELETE -----
@pytest.fixture
def delete_success():
    return {"code": 200, "message": "User deleted successfully"}

# ----- GENERAL -----
@pytest.fixture
def general_error():
    return {"detail": "There was an error"}

@pytest.fixture
def general_internal_server_error():
    return {"detail": "Internal server error"}
