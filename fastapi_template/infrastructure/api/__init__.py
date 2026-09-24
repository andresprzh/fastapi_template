"""HTTP routers, one module per feature."""

from fastapi_template.infrastructure.api.auth import get_auth_router

__all__ = ["get_auth_router"]
