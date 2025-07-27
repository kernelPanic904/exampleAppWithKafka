from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from domain.entities.common.entities_enums import MovementEvent
from domain.entities.product import Product
from domain.entities.warehouse import Warehouse


@dataclass
class Movement:
    movement_id: UUID
    event: MovementEvent
    product: Product
    warehouse: Warehouse
    timestamp: datetime
    quantity: int
    source: str
    destination: str

    id: UUID | None = field(default=None)
