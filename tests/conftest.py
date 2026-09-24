import pytest


@pytest.fixture
def anyio_backend():
    """Run ``@pytest.mark.anyio`` tests on asyncio only.

    The repository, use cases and API layers are async. The pytest plugin that
    runs them ships with ``anyio`` (already a FastAPI dependency), so no extra
    package is needed: mark a coroutine test with ``@pytest.mark.anyio`` and it
    will be awaited using this backend.
    """
    return "asyncio"


@pytest.fixture
async def session_maker(tmp_path):
    """Provide an async SQLAlchemy sessionmaker backed by a temporary SQLite file.

    This fixture creates a per-test SQLite file and initializes the schema so
    tests can use the real repositories against a lightweight file DB.
    """
    from fastapi_template.infrastructure.repositories import init_async_db

    db_file = tmp_path / "test_db.sqlite"
    db_url = f"sqlite+aiosqlite:///{db_file}"
    maker = await init_async_db(db_url)
    return maker
