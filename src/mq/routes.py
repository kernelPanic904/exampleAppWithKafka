from faststream.kafka import KafkaRoute

from mq.handlers.movement import movement_handler


def get_routes() -> list[KafkaRoute]:
    movement_route = KafkaRoute(movement_handler, "arrival")
    return [movement_route]
