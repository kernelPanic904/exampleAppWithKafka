from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from domain.entities.warehouse import Warehouse


class IWarehouseRepository(Protocol):
    @abstractmethod
    async def add(self, warehouse: Warehouse) -> Warehouse: ...

    @abstractmethod
    async def get_by_id(self, warehouse_id: UUID) -> Warehouse | None: ...
