from app.db.models.base_model import Base
from sqlalchemy import Column, Integer, String, DateTime, ARRAY, MetaData, JSON
from datetime import datetime, timezone

class UsersAndPokemons(Base):
    __tablename__ = "users_and_pokemons"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False )
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    role = Column(String(20), default="user")

    # ARRAY is for Postgres database
    #pokemons = Column(ARRAY(Integer), nullable=False)
    # JSON Column is recommended for Cross-Database compatibility
    # Automatically it serializes/deserializes to Python list
    pokemon_ids = Column(JSON, nullable=False, default=list)

    created_at = Column(
        DateTime,
        default=datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )
    
    # Space for relationship

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}',hashed_password='{self.hashed_password}',role='{self.role}',pokemonsIds='{self.pokemon_ids}',created_at='{self.created_at}',updated_at='{self.updated_at}')>"
    

