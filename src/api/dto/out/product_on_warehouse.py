from uuid import UUID

from pydantic import BaseModel


class ProductOnWHDTO(BaseModel):
    product_id: UUID
    warehouse_id: UUID
    quantity: int
