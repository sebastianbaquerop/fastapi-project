from pydantic import BaseModel

class PokemonsDTO(BaseModel):
    id: int
    name: str