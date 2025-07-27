from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from domain.entities.common.entities_enums import MovementEvent


class MovementData(BaseModel):
    movement_id: UUID
    warehouse_id: UUID
    product_id: UUID
    timestamp: datetime
    event: MovementEvent
    quantity: int


class MovementEventInn(BaseModel):
    id: UUID
    source: str
    destination: str
    data: MovementData
