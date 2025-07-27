from dishka import Provider, Scope, provide

from domain.interfaces.repositories.movement import IMovementRepository
from domain.interfaces.repositories.product import IProductRepository
from domain.interfaces.repositories.product_on_wh import IProductOnWHRepository
from domain.interfaces.repositories.warehouse import IWarehouseRepository
from infrastructure.repositories.movement import MovementRepository
from infrastructure.repositories.product import ProductRepository
from infrastructure.repositories.product_on_wh import ProductOnWHRepository
from infrastructure.repositories.warehouse import WarehouseRepository


class RepositoriesProvider(Provider):
    scope = Scope.REQUEST

    movement_repository = provide(
        MovementRepository,
        provides=IMovementRepository,
    )
    product_repository = provide(
        ProductRepository,
        provides=IProductRepository,
    )
    warehouse_repository = provide(
        WarehouseRepository,
        provides=IWarehouseRepository,
    )
    product_on_wh_repository = provide(
        ProductOnWHRepository,
        provides=IProductOnWHRepository,
    )
