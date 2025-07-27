from uuid import UUID

from domain.entities.movement import Movement
from domain.interfaces.repositories.movement import IMovementRepository
from domain.interfaces.repositories.product_on_wh import IProductOnWHRepository


class GetMovementInteractor:
    def __init__(
        self,
        movement_repository: IMovementRepository,
        product_on_wh_repository: IProductOnWHRepository,
    ) -> None:
        self.movement_repository = movement_repository
        self.product_on_wh_repository = product_on_wh_repository

    async def __call__(self, movement_id: UUID) -> list[Movement]:
        movements = await self.movement_repository.get_movements(movement_id)
        return movements
