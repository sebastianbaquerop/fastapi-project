import pytest
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models.base_model import Base
from app.main import app
from fastapi.testclient import TestClient
import respx
from httpx import Response, AsyncClient
from app.core.dependencies import get_http_client
from dotenv import dotenv_values
import os

# Env mode
mode = dotenv_values("envs/.env")
env_mode = mode.get("ENV_MODE", "dev")

# Path env file per environment
env_file = f"{env_mode}.env"
config = {}

# validate if 'env_file existe'
if os.path.exists(f"envs/{env_file}"):
    # Load env variables
    config = dotenv_values(f"envs/{env_file}")
else:
    raise FileNotFoundError(f"Environment file {env_file} not found.")

# Connection settings
USER = config.get("DB_USER")  #'admin'
PASS = config.get("DB_PASS")  #'10102025!'
HOST = config.get("DB_HOST")  #'127.0.0.1'
PORT = config.get("DB_PORT")  #'5432'
DB_NAME = config.get("DB_NAME")  #'take_home_challenge'
IS_TEST_ENV = config.get("IS_TEST_ENV")  # True
POKEMON_API_URL = config.get("POKEMON_API_URL")  # "https://pokeapi.co/api/v2/pokemon/"

# Manage Dev/Prod DB Test
if IS_TEST_ENV == "true":
    SQLARCHEMY_DATABASE_URL = (
        "sqlite:///" + DB_NAME + "_test.db"
    )  # sufix '_test.db' is to isolate the database from original
    print(f"SQLARCHEMY_DATABASE_URL: {SQLARCHEMY_DATABASE_URL}")
else:
    URL.create(
        drivername="postgresql",
        username=USER,
        password=PASS,
        host=HOST,
        port=PORT,
        database=DB_NAME,
    )

# Create DB engine
engine = create_engine(url=SQLARCHEMY_DATABASE_URL)

# Create a sessionmaker to manage sessions
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create table in the database
Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def get_db():
    """Create a new database session with a rollback at the end of the test"""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def test_client(get_db):
    """Create a test client that uses the overrride 'get_db' fixture to return a session."""

    def override_get_db():
        try:
            yield get_db
        finally:
            get_db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def test_health_response():
    """Health check response"""
    return {
        "code": 200,
        "info": {
            "health": "healthy",
            "schemas": "Tables are already presented in the database",
        },
    }


@pytest.mark.asyncio
@respx.mock
async def get_pokemon_data_mock():
    """Mock Pokemon API Call"""
    respx.get(POKEMON_API_URL + "1").mock(
        return_value=Response(
            status_code=200,
            json={
                "id": 1,  # id is a field of the Pokemon API response
                "name": "name",  # name is a field of the Pokemon API response
            },
        )
    )


@pytest.mark.asyncio
@respx.mock
async def get_pokemon_data_error_mock(pokemon_id: int):
    """Mock Pokemon API Call"""
    respx.get(POKEMON_API_URL + pokemon_id).mock(
        return_value=Response(status_code=500, json={"error": "Server error"})
    )


@pytest.fixture
def mock_http_client():
    with respx.mock as router:

        async def override_get_http_client():
            async with AsyncClient() as client:
                yield client

        app.dependency_overrides[get_http_client] = override_get_http_client
        yield router
        app.dependency_overrides.clear()
