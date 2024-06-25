from faststream.kafka.broker import KafkaBroker
from faststream import FastStream

from settings import get_settings
from consumers.handlers import router


def get_app():
    settings = get_settings()
    broker = KafkaBroker(settings.KAFKA_BROKER_URL)
    broker.include_router(router=router)

    return FastStream(broker=broker)
