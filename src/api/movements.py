from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from api.dto.out.movement import MovementDTO
from application.interactors.get_movement import GetMovementInteractor


movements_router = APIRouter(prefix="/movements")


@movements_router.get(path="/{movement_id}")
@inject
async def get_movement_by_id(
    movement_id: UUID,
    interactor: FromDishka[GetMovementInteractor],
) -> None:
    movements = await interactor(movement_id)
    return [
        MovementDTO(
            id=movement.id,
            movement_id=movement.movement_id,
            event=movement.event,
            timestamp=movement.timestamp,
            source=movement.source,
            destination=movement.destination,
            quantity=movement.quantity,
        )
        for movement in movements
    ]
