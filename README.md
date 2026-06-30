
1. Scaffold 
   - api/ # API endpoints (GET, POST, PATCH, PUT, DELETE) ✅
   - core/ (call external APIs, configs, security) ✅
   - db/ (Tables Models) ✅
   - repositories/ (behavior to database) ✅
   - schemas/ #Pydantic models (DTOs - Requests & Responses) ✅
   - services/ # Business logic and external api calls ✅
   - test/ #Test Features (Integration Test, Unit Test) ✅
   - requirements.txt # Dependencies
   - .env # Secrets
   - config.py # Environment variables
2. APIs
   - Users ✅
   - Users V2 ✅
3. Versioning ✅


Steps:
1. MVP:
   1. Create a project that runs using FastAPI framework ✅
   2. Create Scaffold of the project ✅
   3. Create scaffold APIs ✅
   4. Swagger ✅
   5. Version the APIs ✅
2. Add DTOs, Database, Schemas ✅
3. Repositories works 
   - Create ✅
   - Delete ✅
   - Get one ✅
   - Update ✅
   - Get all ✅
   - Patch ✅
   **Nota: Improvement of get method using paginator behavior
4. Update Swaggers and review behavior ✅
5. Docker & Docker Compose for DB ✅
   - You must to have installed docker in your machine
   - Run the command on the folder project that run the content of 'docker-componse.yml'
      ```
      docker compose up
      ```
   **Nota: Improvement to valida if the database exist and the tables exist ✅
6. External Dependencies (Pokemon APIs) ✅
7. Testing 
   - Set up:
     - DB Testing
     - Mock External Dependencies (E.g. Pokemon API)
8. Env Variables
9. Deployed
10. Ignore 
11. Linter 
12. Formatter 
13. Dockerize all the project
14. Readme 
15. Deployement or Release
16. Exercise

Dependencies:
- pip install virtualenv
  - python3 -m venv .venv
- pip install fastapi[standard]
- pip install uvicorn
- pip install sqlalchemy
- pip install psycopg2-binary # For testing/development
- pip install psycopg2 # postgresql adapter for producction
- pip install httpx
- pip install tenacity

Settings:
- all the folder inside 'app' must have the file '__init__.py'
- pyproject.toml set the following:
´´´
[tool.fastapi]
entrypoint = "app.main:app"
´´´
- to run the application you cursor on terminal will be inside folder project an execute the fastapi command:
´´´
fastapi dev 
´´´
or the contrary 
´´´
fastapi dev app.main
´´´

- Recomendations:
1. Review carefully the data base models inside 'db/models' folder
2. Load database and create table firstly by code 'Base.metadata.create_all(bind=engine)'
3. ORM is implemented by 'Base' that has 'declarative_base()' from SQLalchemy ORM (Object-Relational Mapping)
4. Pydantic is a library for automatic request and response validation, serialization, and interactive API Documentation
   Request and response schemas are commonly placed to 'schemas' folder.

