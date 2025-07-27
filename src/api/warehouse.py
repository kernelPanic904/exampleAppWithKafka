from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from api.dto.out.product_on_warehouse import ProductOnWHDTO
from application.interactors.get_product_on_wh import GetProductOnWHInteractor


warehouse_router = APIRouter(prefix="/warehouse")


@warehouse_router.get(path="/{warehouse_id}/products/{product_id}")
@inject
async def get_product_on_warehouse(
    warehouse_id: UUID,
    product_id: UUID,
    interactor: FromDishka[GetProductOnWHInteractor],
) -> ProductOnWHDTO:
    product_on_warehouse = await interactor(product_id, warehouse_id)
    return ProductOnWHDTO(
        product_id=product_on_warehouse.product_id,
        warehouse_id=product_on_warehouse.warehouse_id,
        quantity=product_on_warehouse.quantity,
    )
