from dishka import Provider, Scope, from_context

from core.config import DBConfig, Config, MQConfig


class AppContextProvider(Provider):
    scope = Scope.APP

    config = from_context(provides=Config)
    db_config = from_context(provides=DBConfig)
    mq_config = from_context(provides=MQConfig)
