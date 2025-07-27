from fastapi import APIRouter

from api.movements import movements_router
from api.warehouse import warehouse_router


root_router = APIRouter(prefix="/api")
root_router.include_router(movements_router)
root_router.include_router(warehouse_router)
