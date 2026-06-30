from fastapi import Request
from app.core.http_client import HTTPClient

async def get_http_client(request: Request) -> HTTPClient:
    """
    Injects the shared HTTP client from app.state.
    """
    if hasattr(request.app.state, "http_client"):
        return request.app.state.http_client
    if hasattr(request.app, "root") and hasattr(request.app.root.state, "http_client"):
        return request.app.root.state.http_client
    raise RuntimeError("HTTP Client not initialized. Check lifespan startup.")