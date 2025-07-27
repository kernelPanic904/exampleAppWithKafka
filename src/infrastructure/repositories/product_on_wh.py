from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.product_on_wh import ProductOnWarehouse
from domain.interfaces.repositories.product_on_wh import IProductOnWHRepository


class ProductOnWHRepository(IProductOnWHRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(
        self,
        product_on_wh: ProductOnWarehouse,
    ) -> ProductOnWarehouse:
        self._session.add(product_on_wh)

    async def get(
        self,
        warehouse_id: UUID,
        product_id: UUID,
    ) -> ProductOnWarehouse | None:
        stmt = select(ProductOnWarehouse).where(
            ProductOnWarehouse.warehouse_id == warehouse_id,
            ProductOnWarehouse.product_id == product_id,
        )
        product_on_warehouse = await self._session.scalar(stmt)
        if not product_on_warehouse:
            return None
        return product_on_warehouse
