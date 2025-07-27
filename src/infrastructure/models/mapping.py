from uuid import uuid4

from sqlalchemy import (
    UUID,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
)
from sqlalchemy.orm import relationship

from domain.entities.movement import Movement
from domain.entities.product import Product
from domain.entities.warehouse import Warehouse
from domain.entities.product_on_wh import ProductOnWarehouse
from infrastructure.models.registry import mapper_registry


warehouse_table = Table(
    "warehouses",
    mapper_registry.metadata,
    Column("id", UUID, primary_key=True),
)

warehouse_product_assoc_table = Table(
    "warehouse_product_association",
    mapper_registry.metadata,
    Column("id", UUID, primary_key=True, default=uuid4),
    Column(
        "warehouse_id",
        UUID,
        ForeignKey("warehouses.id"),
    ),
    Column(
        "product_id",
        UUID,
        ForeignKey("products.id"),
    ),
    Column("quantity", Integer),
)

product_table = Table(
    "products",
    mapper_registry.metadata,
    Column("id", UUID, primary_key=True),
)

movement_table = Table(
    "movements",
    mapper_registry.metadata,
    Column("id", UUID, primary_key=True, default=uuid4),
    Column("movement_id", UUID, default=uuid4, index=True, nullable=False),
    Column("event", String(50), index=True),
    Column("product_id", UUID, ForeignKey("products.id")),
    Column("warehouse_id", UUID, ForeignKey("warehouses.id")),
    Column("timestamp", DateTime()),
    Column("source", String()),
    Column("destination", String()),
    Column("quantity", Integer),
)


def start_mapping() -> None:
    mapper_registry.map_imperatively(
        Movement,
        movement_table,
        properties={
            "product": relationship(Product),
            "warehouse": relationship(Warehouse),
        },
    )

    mapper_registry.map_imperatively(
        Product,
        product_table,
        properties={
            "warehouses": relationship(
                Warehouse,
                secondary="warehouse_product_association",
                back_populates="products",
            ),
        },
    )

    mapper_registry.map_imperatively(
        Warehouse,
        warehouse_table,
        properties={
            "products": relationship(
                Product,
                secondary="warehouse_product_association",
                back_populates="warehouses",
            ),
        },
    )

    mapper_registry.map_imperatively(
        ProductOnWarehouse,
        warehouse_product_assoc_table,
    )
