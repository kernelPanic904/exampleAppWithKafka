from datetime import datetime
from uuid import UUID

from core.logger import logger
from domain.entities.common.entities_enums import MovementEvent
from domain.entities.movement import Movement
from domain.entities.product import Product
from domain.entities.product_on_wh import ProductOnWarehouse
from domain.entities.warehouse import Warehouse
from domain.interfaces.repositories.movement import IMovementRepository
from domain.interfaces.repositories.product import IProductRepository
from domain.interfaces.repositories.product_on_wh import IProductOnWHRepository
from domain.interfaces.repositories.warehouse import IWarehouseRepository
from domain.interfaces.uow import IUOW
from mq.dto.inn.movement_event import MovementEventInn


class ProductMovementInteractor:
    def __init__(
        self,
        uow: IUOW,
        movement_repository: IMovementRepository,
        product_repository: IProductRepository,
        warehouse_repository: IWarehouseRepository,
        product_on_wh_repository: IProductOnWHRepository,
    ) -> None:
        self.uow = uow
        self.movement_repository = movement_repository
        self.product_repository = product_repository
        self.warehouse_repository = warehouse_repository
        self.product_on_wh_repository = product_on_wh_repository

    async def get_or_create_warehouse(self, warehouse_id: UUID) -> Warehouse:
        logger.debug("Get or create warehouse...")
        warehouse = await self.warehouse_repository.get_by_id(warehouse_id)
        if not warehouse:
            warehouse = Warehouse(id=warehouse_id)
            await self.warehouse_repository.add(warehouse)
        return warehouse

    async def get_or_create_product(self, product_id: UUID) -> Product:
        logger.debug("Get or create product...")
        product = await self.product_repository.get_by_id(product_id)
        if not product:
            product = Product(id=product_id)
            await self.product_repository.add(product)
        return product

    async def get_or_create_product_on_wh(
        self,
        warehouse_id: UUID,
        product_id: UUID,
    ) -> ProductOnWarehouse:
        logger.debug("Get or create product on warehouse...")
        product_on_warehouse = await self.product_on_wh_repository.get(
            warehouse_id=warehouse_id,
            product_id=product_id,
        )
        logger.debug("Product on warehouse: {}".format(product_on_warehouse))
        if not product_on_warehouse:
            product_on_warehouse = ProductOnWarehouse(
                warehouse_id=warehouse_id,
                product_id=product_id,
            )
            await self.product_on_wh_repository.add(product_on_warehouse)
            logger.debug("Created: {}".format(product_on_warehouse))
        return product_on_warehouse

    async def create_movement(
        self,
        movement_id: UUID,
        warehouse: Warehouse,
        product: Product,
        event: MovementEvent,
        timestamp: datetime,
        source: str,
        destination: str,
        quantity: str,
    ) -> Movement:
        logger.debug("Create movement...")
        movement = Movement(
            movement_id=movement_id,
            event=event,
            product=product,
            warehouse=warehouse,
            timestamp=timestamp,
            source=source,
            destination=destination,
            quantity=quantity,
        )
        await self.movement_repository.add(movement)
        return movement

    async def __call__(self, message: MovementEventInn) -> None:
        logger.debug("Start process movement...")
        data = message.data

        warehouse = await self.get_or_create_warehouse(data.warehouse_id)
        product = await self.get_or_create_product(data.product_id)

        await self.uow.flush()

        product_on_warehouse = await self.get_or_create_product_on_wh(
            warehouse_id=warehouse.id,
            product_id=product.id,
        )
        movement = await self.create_movement(
            movement_id=data.movement_id,
            warehouse=warehouse,
            product=product,
            event=data.event,
            timestamp=data.timestamp,
            source=message.source,
            destination=message.destination,
            quantity=data.quantity,
        )

        if movement.event == MovementEvent.arrival:
            product_on_warehouse.add_quantity(data.quantity)
        if movement.event == MovementEvent.departure:
            product_on_warehouse.substract_quantity(data.quantity)

        await self.uow.commit()
