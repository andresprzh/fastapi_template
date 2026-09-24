from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi_template.infrastructure.repositories import (
    init_async_db,
    SQLAlchemyUserRepository,
)
from fastapi_template.application.use_cases.auth import AuthUseCase
from fastapi_template.infrastructure.api import (
    get_auth_router,
)


# Provide OpenAPI metadata and disable default docs URLs so we can customize
app = FastAPI(
    title="FastAPI Template (Layered)",
    description="""FastAPI Template with a layered architecture,
    including domain models, use cases, and infrastructure
    (repositories and API routers).""",
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url="/openapi.json",
)


@app.on_event("startup")
async def startup():
    """Initialize the async DB and register routers when the app starts.

    Doing DB initialization here avoids calling `asyncio.run` from code that
    may already be running inside an event loop (this happens with
    `uvicorn --reload`).
    """
    session_maker = await init_async_db()

    user_repo = SQLAlchemyUserRepository(session_maker)

    auth_uc = AuthUseCase(user_repo)

    app.include_router(get_auth_router(auth_uc))


@app.get("/", include_in_schema=False)
async def custom_swagger_ui():
    """Serve Swagger UI using FastAPI's built-in helper.

    No extra dependency required — FastAPI includes Swagger UI and ReDoc endpoints.
    """
    return get_swagger_ui_html(
        openapi_url=app.openapi_url, title=f"{app.title} - Swagger UI"
    )
