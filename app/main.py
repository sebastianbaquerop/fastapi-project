from fastapi import FastAPI
from app.api.v1 import routes as v1_router

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
    },
)

app_v1.include_router(v1_router.router)

# Root App
app = FastAPI(
    title="Take Home Challenge API Gateway",
    description="Select a version below or visit /docs/v1, /docs/v2",
    docs_url=None,
    openapi_url=None
)

app.mount("/v1", app_v1, name="API version 1")


@app.get("/", tags=["App"])
async def root():
    return {
        "message": "API Gateway",
        "documentation": {
            "v1": "/v1/docs"
        }
    }


