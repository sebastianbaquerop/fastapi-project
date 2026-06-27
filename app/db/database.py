from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models.base_model import Base

# 1. Connection settings
USER = 'admin'
PASS = '10102025!'
HOST = '127.0.0.1'
PORT = '5432'
DB = 'take_home_challenge'
IS_TEST_ENV = True

print(f"Localhost: {HOST}")
if IS_TEST_ENV is True:
    SQLARCHEMY_DATABASE_URL = 'sqlite:///take_home_challenge.db'
    print('Test DB')
else:
    """Createing the database connection to the Postgresql database"""
    SQLARCHEMY_DATABASE_URL = URL.create(
        drivername="postgresql",
        username=USER,
        password=PASS,
        host=HOST,
        port=PORT,
        database=DB
    )
    print('Prod DB')

engine = create_engine(url=SQLARCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine) # Generate the schemas at once in our target SQLite/Postgres database

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if IS_TEST_ENV is False:
    init_db()