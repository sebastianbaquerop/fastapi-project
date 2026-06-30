from fastapi import FastAPI
from app.api.v1 import routes as v1_router
from app.api.v2 import routes as v2_router
from contextlib import asynccontextmanager
from app.core.http_client import HTTPClient

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create Singleton
    print("Initializing shared HTTP Client...")
    try:
        app.state.http_client = HTTPClient()
        print("SUCCESS: Client initialized")
    except Exception as e:
        print(f"FAILED: {e}")
        raise
    # Shutdown: Cleanup Resource
    print("Closing HTTP Client...")
    yield
    await app.state.http_client.close()

# Root App (Gateway) - Lifespan attached HERE
app = FastAPI(
    title="Take Home Challenge API Gateway",
    description="Select a version below or visit /docs/v1, /docs/v2",
    docs_url=None,
    openapi_url=None,
    lifespan=lifespan
)

# API v1
app_v1 = FastAPI(
    title="Take Home Challenge API Gateway",
    description="Clean architecture FastAPI with authentication",
    docs_url="/docs",
    openapi_prefix="/v1",
    openapi_url="/openapi/v1.json",
    version="1.0.0",
    contact={
        "name": "Sebastian Baquero",
        "email": "sebastian.baquero.p@gmail.com.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# API v2
app_v2 = FastAPI(
    title="Take Home Challenge API Gateway",
    description="Clean architecture FastAPI with authentication and Poken API",
    docs_url="/docs",
    openapi_prefix="/v2",
    openapi_url="/openapi/v2.json",
    version="1.0.0",
    contact={
        "name": "Sebastian Baquero",
        "email": "sebastian.baquero.p@gmail.com.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# Link 'state' to root app to use HTTPClient inside API versions
app_v1.state = app.state
app_v2.state = app.state

app_v1.include_router(v1_router.router)
app_v2.include_router(v2_router.router)

app.mount("/v1", app_v1, name="API version 1")
app.mount("/v2", app_v2, name="API version 2")


@app.get("/", tags=["App"])
async def root():
    return {
        "message": "API Gateway",
        "documentation": {
            "v1": "/v1/docs"
        }
    }


