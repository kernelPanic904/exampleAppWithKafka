from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from domain.entities.product import Product


class IProductRepository(Protocol):
    @abstractmethod
    async def add(self, product: Product) -> None: ...

    @abstractmethod
    async def get_by_id(self, product_id: UUID) -> Product | None: ...
