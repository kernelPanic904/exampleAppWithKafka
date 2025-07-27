from dishka import Provider, Scope, provide

from application.interactors.get_movement import GetMovementInteractor
from application.interactors.get_product_on_wh import GetProductOnWHInteractor
from application.interactors.product_movement import ProductMovementInteractor


class InteractorsProvider(Provider):
    scope = Scope.REQUEST

    movement_event_interactor = provide(ProductMovementInteractor)
    get_movement_interactor = provide(GetMovementInteractor)
    get_product_on_warehouse_interactor = provide(GetProductOnWHInteractor)
