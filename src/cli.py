from dishka.integrations.fastapi import setup_dishka as setup_fastapi
from dishka.integrations.faststream import setup_dishka as setup_faststream
from fastapi import FastAPI
from faststream import FastStream
from faststream.kafka import KafkaBroker, KafkaRouter

from api.root_router import root_router
from core.config import get_config
from di.ioc import get_container
from infrastructure.models.mapping import start_mapping
from mq.routes import get_routes


def get_application() -> FastAPI:
    start_mapping()

    container = get_container()
    config = get_config()

    broker = KafkaBroker(f"{config.mq_config.host}:{config.mq_config.port}")
    kafka_router = KafkaRouter(handlers=get_routes())
    broker.include_router(kafka_router)
    setup_faststream(container, FastStream(broker))

    app = FastAPI(
        on_startup=[broker.start],
        on_shutdown=[broker.stop],
    )
    app.include_router(root_router)
    setup_fastapi(container, app)

    return app
