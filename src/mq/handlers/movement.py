from dishka.integrations.faststream import FromDishka, inject

from application.interactors.product_movement import ProductMovementInteractor
from mq.dto.inn.movement_event import MovementEventInn


@inject
async def movement_handler(
    data: MovementEventInn,
    interactor: FromDishka[ProductMovementInteractor],
) -> None:
    await interactor(data)
