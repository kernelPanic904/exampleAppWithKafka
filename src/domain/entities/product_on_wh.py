from dataclasses import dataclass, field
from uuid import UUID

from core.logger import logger
from domain.exceptions import ProductOnWarehouseQuantityLessZero


@dataclass
class ProductOnWarehouse:
    warehouse_id: UUID
    product_id: UUID
    quantity: int = field(default_factory=int)

    def add_quantity(self, value: int) -> None:
        logger.debug("Add quantity... {} + {}".format(self.quantity, value))
        self.quantity += value

    def substract_quantity(self, value: int) -> None:
        logger.debug("Sub quantity... {} - {}".format(self.quantity, value))
        result = self.quantity - value

        if result < 0:
            raise ProductOnWarehouseQuantityLessZero(
                message=(
                    "Product on warehouse cannot be less than 0, "
                    "current quantity: {current_quantity}, value: {value}, "
                    "result: {result}"
                ).format(
                    current_quantity=self.quantity,
                    value=value,
                    result=result,
                )
            )
        self.quantity = result
