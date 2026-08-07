from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models.base_model import Base
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

print(f"DB_NAME: {DB_NAME}")
# Manage Dev/Prod DB
if IS_TEST_ENV == "true":
    SQLARCHEMY_DATABASE_URL = "sqlite:///" + DB_NAME + ".db"
    print("Test DB (SQLite)")
else:
    """Createing the database connection to the Postgresql database"""
    SQLARCHEMY_DATABASE_URL = URL.create(
        drivername="postgresql",
        username=USER,
        password=PASS,
        host=HOST,
        port=PORT,
        database=DB_NAME,
    )
    print("Prod DB (Postgres)")

# Create DB engine
engine = create_engine(url=SQLARCHEMY_DATABASE_URL)


# Create a sessionmaker to manage sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(
        bind=engine
    )  # Generate the schemas at once in our target SQLite/Postgres database

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if IS_TEST_ENV is False:
    init_db()
