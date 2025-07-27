from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.product import Product
from domain.interfaces.repositories.product import IProductRepository


class ProductRepository(IProductRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, product: Product) -> None:
        self._session.add(product)

    async def get_by_id(self, product_id: UUID) -> Product | None:
        stmt = select(Product).where(Product.id == product_id)
        product = await self._session.scalar(stmt)
        if not product:
            return None
        return product
