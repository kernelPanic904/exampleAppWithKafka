from uuid import UUID
from domain.entities.product_on_wh import ProductOnWarehouse
from domain.interfaces.repositories.product_on_wh import IProductOnWHRepository


class GetProductOnWHInteractor:
    def __init__(
        self,
        product_on_wh_repository: IProductOnWHRepository,
    ) -> None:
        self.product_on_wh_repository = product_on_wh_repository

    async def __call__(
        self,
        product_id: UUID,
        warehouse_id: UUID,
    ) -> ProductOnWarehouse:
        return await self.product_on_wh_repository.get(
            warehouse_id=warehouse_id,
            product_id=product_id,
        )
