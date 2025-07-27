from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.warehouse import Warehouse
from domain.interfaces.repositories.warehouse import IWarehouseRepository


class WarehouseRepository(IWarehouseRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, warehouse: Warehouse) -> Warehouse:
        self._session.add(warehouse)

    async def get_by_id(self, warehouse_id: UUID) -> Warehouse | None:
        stmt = select(Warehouse).where(Warehouse.id == warehouse_id)
        warehouse = await self._session.scalar(stmt)
        if not warehouse:
            return None
        return warehouse
