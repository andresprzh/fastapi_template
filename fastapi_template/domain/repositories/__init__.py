"""Repository interfaces the domain requires, one module per feature.

These are abstract on purpose: the domain declares what it needs, and
``fastapi_template.infrastructure.repositories`` supplies the implementations.
"""

from fastapi_template.domain.repositories.user import UserRepository

__all__ = ["UserRepository"]
