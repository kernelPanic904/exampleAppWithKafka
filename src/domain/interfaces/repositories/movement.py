from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from domain.entities.movement import Movement


class IMovementRepository(Protocol):
    @abstractmethod
    async def add(self, movement: Movement) -> None: ...

    @abstractmethod
    async def get_movements(self, movement_id: UUID) -> list[Movement]: ...
