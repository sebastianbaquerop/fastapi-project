from fastapi import APIRouter

from app.api.v2.endpoints import users as user_router
from app.api.v1.endpoints import health as health_router

# Create the master router for v2
router = APIRouter()

# Include features routers
router.include_router(user_router.router)
router.include_router(health_router.router)