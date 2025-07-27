from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.movement import Movement
from domain.interfaces.repositories.movement import IMovementRepository


class MovementRepository(IMovementRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, movement: Movement) -> None:
        self._session.add(movement)

    async def get_movements(self, movement_id: UUID) -> list[Movement]:
        stmt = select(Movement).where(Movement.movement_id == movement_id)
        movements = await self._session.scalars(stmt)
        return movements
