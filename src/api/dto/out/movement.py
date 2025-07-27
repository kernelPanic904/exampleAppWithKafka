from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from domain.entities.common.entities_enums import MovementEvent


class MovementDTO(BaseModel):
    id: UUID
    movement_id: UUID
    event: MovementEvent
    timestamp: datetime
    source: str
    destination: str
    quantity: int
