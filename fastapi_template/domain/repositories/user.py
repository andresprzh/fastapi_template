from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from fastapi_template.domain.models import User


class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def get(self, id: UUID) -> Optional[User]:
        pass

    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[User]:
        pass
