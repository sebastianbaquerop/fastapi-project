# FastAPI Project

1. Scaffold
   - api/ # API endpoints (GET, POST, PATCH, PUT, DELETE) ✅
   - core/ (call external APIs, configs, security) ✅
   - db/ (Tables Models) ✅
   - repositories/ (behavior to database) ✅
   - schemas/ #Pydantic models (DTOs - Requests & Responses) ✅
   - services/ # Business logic and external api calls ✅
   - test/ #Test Features (Integration Test, Unit Test)
   - requirements.txt # Dependencies pip install -r requirements.txt
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
      ```docker compose up```
   **Nota: Improvement to valida if the database exist and the tables exist ✅
6. External Dependencies (Pokemon APIs) ✅
7. Testing
   - Best practices: ✅
     - Tests shoud be isolated
     - Tests should be independents
     - Tests should berepeatable
     - Tests should be readable
     - Tests should be fast
     - Tests should be a part of the commit and build process
     - Tests should use single 'assert' per test
     - Tests should use fake data/database
   - Recomendations: ✅
     - Use Dependency Injections
     - Use Pytest because it is a python test framework than enhance the testing practice.
     - Key amongs:
     - conftest.py:
       - Serves as a central place of fixture definitions, making them accessible across multiple test files, promoting reuse and reduce code duplication
     - Pytest fixtures:
       - Offer a powerfull way to setup and tear down resources needed for tests, ensuring isolation and reliability
     - Pytest parametrization:
       - Allow for the easy creation of multiple test cases from a single test function.
   - Set up:
     - DB Testing ✅
     - Mock DTOs ✅
     - Mock External Dependencies (E.g. Pokemon API) ✅
       - If you use 'httpx' library you should use 'respx' to mock aysnc API calls
   - Integration Test ✅ (At the same level of 'app' folder)
     - ```pytest tests/``` #It will execute 26 tests: 13 test of v1 and 13 tests of v2
     - ```pytest -v tests/``` To show high level results
     - ```pytest -vv integrations/``` To show information differences for debuggin
     - ```pytest -s tests/``` # To show information by```print()```
     - Specific test with logs:
     - ```pytest -s tests/integrations/v2/test_users_pokemons.py::test_health```
     - Specific test without logs:
     - ```pytest -v tests/integrations/v2/test_users_pokemons.py::test_health```
   - Coverage: ✅
     - 96%
     - instalation: pip install coverage
     - execute coverage:
       - coverage run:
         - Common use (At the same level of 'app' folder):
           - Ex: ```coverage run -m pytest tests/```
       - coverage report: ```coverage report -m```
       - html report: ```coverage html``` #it will write html report to Wrote HTML report location ```htmlcov/index.html```
8. Env Variables ✅
   1. library ```pip install python-dotenv```
   2. One env
   3. Multiple envs
9. Git ignore ✅
10. Linter
    1. Ruff
        1. Installation:
           ```pip install ruff```
        2. Rules:

            ```ruby
            [tool.ruff]
            line-length = 77
            target-version = "py311" # Cambia a tu versión de Python (py310, py312, etc.)
            [tool.ruff.lint]
            # E, W = Estilo PEP8
            # F = Código muerto y variables no usadas
            # I = Orden de importaciones (isort)
            # B = Buenas prácticas y bugs comunes (bugbear)
            # UP = Actualizaciones de sintaxis moderna de Python (pyupgrade)
            select = ["E", "F", "W", "I", "B", "UP"]
            # Evita alertas molestas por dependencias inyectadas en FastAPI
            ignore = [
            "B008", # Permite poner llamadas a funciones en argumentos (ej: Depends(get_db))
            ]
            [tool.ruff.lint.per-file-ignores]
            "**/__init__.py" = ["F401"] # Ignora imports no usados en el archivo inicial de tu app o rutas
            ```

        3. Check rules:
          ```ruff check``` # Lint all files in the current directory.
11. Formatter ✅
    1. Ruff
        1. Instalation:
            ```pip install ruff```
        2. Rules:

             ```ruby
             [tool.ruff.format]
             quote-style = "double" # Like Black, use double quotes for strings.
             skip-magic-trailing-comma = false # Like Black, respect magic trailing.
             indent-style = "space  # Like Black, indent with spaces, rather than tabs.
             ```

        3. Check format:
             ```ruff format``` # Format all files in the current directory.
12. Dockerize API project
    1. Dockerfile
    2. Create docker image: ```docker build -t image-name:tag .```
    3. Run docker image:
       1. Detached Mode:
       Run the container in the background using the -d flag. This allows you to continue using your terminal while the container runs ```docker run -d image_name:tag```
       2. Interactive Mode: Use the -it flags to run the container and attach your terminal to it, allowing you to interact with the shell inside the container ```docker run -it image-name:tag /bin/bash```
13. Docker Compose (API and DB):
    1. Docker compose file
    2. Run docker compose file:
       1. Build docker compose:
        ```docker-compose build```
       2. Run application:
        ```docker-compose up```
       3. Stop and remove container:
        ```docker-compose down```  
14. Readme
15. . Deployement or Release
16. Coveralls
17. Circle CI
18. Exercise

Dependencies:

```bash
  pip install virtualenv
  python3 -m venv .venv
  pip install fastapi[standard]
  pip install uvicorn
  pip install sqlalchemy
  pip install psycopg2-binary # For testing/development
  pip install psycopg2 # postgresql adapter for producction
  pip install httpx
  pip install tenacity
  pip install pytest
  pip install coverage
  pip install respx
  pip install ruff
```

Settings:

- all the folder inside 'app' must have the file '__init__.py'
- pyproject.toml set the following:
´´´
[tool.fastapi]
entrypoint = "app.main:app"
´´´
- to run the application you cursor on terminal will be inside folder project an execute the fastapi command:
```fastapi dev```
or the contrary
```fastapi dev app.main```

- Recomendations:

1. Review carefully the data base models inside 'db/models' folder
2. Load database and create table firstly by code 'Base.metadata.create_all(bind=engine)'
3. ORM is implemented by 'Base' that has 'declarative_base()' from SQLalchemy ORM (Object-Relational Mapping)
4. Pydantic is a library for automatic request and response validation, serialization, and interactive API Documentation
   Request and response schemas are commonly placed to 'schemas' folder.
5. Moto is a library that allows your tests to easily mock out AWS Services.
