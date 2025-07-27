from dataclasses import dataclass, field
from uuid import UUID

from domain.entities.warehouse import Warehouse


@dataclass
class Product:
    id: UUID
    warehouses: list[Warehouse] = field(default_factory=list)
