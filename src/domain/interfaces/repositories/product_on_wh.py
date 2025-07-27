from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from domain.entities.product_on_wh import ProductOnWarehouse


class IProductOnWHRepository(Protocol):
    @abstractmethod
    async def add(self, product_on_warehouse: ProductOnWarehouse) -> None: ...

    @abstractmethod
    async def get(
        self,
        warehouse_id: UUID,
        product_id: UUID,
    ) -> ProductOnWarehouse | None: ...
