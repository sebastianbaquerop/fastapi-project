from sqlalchemy.orm import Session
from app.repositories.user_and_pokemon_repository import UserAndPokemonRepository
from app.schemas.user_and_pokemon_dto import UserAndPokemonsCreateDTO, UserAndPokemonsDTO, UserAndPokemonsPatchDTO, UsersAndPokemonsDTO
from app.schemas.pokemon_dto import PokemonsDTO
from typing import Optional, List
from app.core.http_client import HTTPClient

class UserAndPokemonService:

    def __init__(self, db_session: Session, http_client: HTTPClient):
        self.repository = UserAndPokemonRepository(db_session)
        self.client = http_client
        self.pokemon_api_url = "https://pokeapi.co/api/v2/pokemon/"
    
    async def get_pokemon_data(self, pokemon_id: int):
        """Internal helper to call external API."""
        response_data = await self.client.get(self.pokemon_api_url+pokemon_id)

        return {
            "id": response_data.get("id"), # id is a field of the Pokemon API response
            "name": response_data.get("name")  # name is a field of the Pokemon API response
        }

    
    def create_user(self, user_data: UserAndPokemonsCreateDTO) -> UsersAndPokemonsDTO:
        user_and_pokemons = self.repository.get_by_email(user_data.email)
        print(f"create_user - user_and_pokemons =======> {user_and_pokemons}")
        if user_and_pokemons:
            raise ValueError("Email already registered")
        user_and_pokemons = self.repository.create(user_data)
        print(f"create_user - user_and_pokemons =======> {user_and_pokemons}")
        user_and_pokemons_dto = UsersAndPokemonsDTO.model_validate(user_and_pokemons)
        print(f"create_user - user_and_pokemons_dto =======> {user_and_pokemons_dto}")
        return user_and_pokemons_dto

    def get_users(self)->List[UsersAndPokemonsDTO]:
        users_and_pokemons = self.repository.list()
        users_and_pokemons_dto_list = [UsersAndPokemonsDTO.model_validate(user) for user in users_and_pokemons]
        return users_and_pokemons_dto_list
    
    async def get_user_by_id(self, user_id: int) -> Optional[UserAndPokemonsDTO]:
        users_and_pokemons = self.repository.get_by_id(user_id)
        if not users_and_pokemons:
            raise ValueError("There was an error")
        pokemons: List[PokemonsDTO] = []
        pokemon_ids =  users_and_pokemons.pokemon_ids
        for id in pokemon_ids:
            json_response =  await self.get_pokemon_data(str(id))
            pokemon_dto = PokemonsDTO.model_validate(json_response)
            pokemons.append(pokemon_dto)
        users_and_pokemons_dto = UsersAndPokemonsDTO.model_validate(users_and_pokemons)
        user_and_pokemons_dict = UserAndPokemonsDTO.model_dump(users_and_pokemons_dto)
        user_and_pokemons_dict["pokemons"] = pokemons
        user_and_pokemons_dto = UserAndPokemonsDTO.model_validate(user_and_pokemons_dict)
        return user_and_pokemons_dto
    
    def update_user(self, user_id: int, user_data: UserAndPokemonsCreateDTO) -> Optional[UsersAndPokemonsDTO]:
         user_and_pokemons = self.repository.update(user_id, user_data)
         if not user_and_pokemons:
             raise ValueError("There was an error")
         user_and_pokemons_dto = UsersAndPokemonsDTO.model_validate(user_and_pokemons)
         return user_and_pokemons_dto
    
    def patch_user(self, user_id: int, user_data: UserAndPokemonsPatchDTO) -> Optional[UsersAndPokemonsDTO]:
         user_and_pokemons = self.repository.patch(user_id, user_data)
         if not user_and_pokemons:
             raise ValueError("There was an error")
         user_and_pokemons_dto = UsersAndPokemonsDTO.model_validate(user_and_pokemons)
         return user_and_pokemons_dto
    
    def delete_user(self, user_id: int) -> bool:
        user_and_pokemons = self.repository.delete(user_id)
        if not user_and_pokemons:
            raise ValueError("There was an error")
        return user_and_pokemons
