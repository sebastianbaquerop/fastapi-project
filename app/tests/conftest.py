import pytest
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models.base_model import Base
from app.main import app
from fastapi.testclient import TestClient
import respx
from httpx import Response, AsyncClient
from app.core.dependencies import get_http_client

# Connection settings
USER = 'admin'
PASS = '10102025!'
HOST = '127.0.0.1'
PORT = '5432'
DB = "take_home_challenge_test"
IS_TEST_ENV = True
POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"

# Manage Dev/Prod DB Test
if IS_TEST_ENV:
    SQLARCHEMY_DATABASE_URL = "sqlite:///"+DB+".db"
else:
    URL.create(
        drivername="postgresql",
        username=USER,
        password=PASS,
        host=HOST,
        port=PORT,
        database=DB
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
    "schemas": "Tables are already presented in the database"
    }
  }

@pytest.mark.asyncio
@respx.mock
async def get_pokemon_data_mock():
    """Mock Pokemon API Call"""
    respx.get(POKEMON_API_URL+"1").mock(
        return_value=Response(
            status_code=200,
            json={
            "id": 1, # id is a field of the Pokemon API response
            "name": "name"  # name is a field of the Pokemon API response
            }
        )
    )   

@pytest.mark.asyncio
@respx.mock
async def get_pokemon_data_error_mock(pokemon_id: int):
    """Mock Pokemon API Call"""
    respx.get(POKEMON_API_URL+pokemon_id).mock(
        return_value=Response(
            status_code=500,
            json={
            "error": "Server error" 
            }
        )
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