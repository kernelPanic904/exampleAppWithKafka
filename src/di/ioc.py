from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import FastapiProvider

from core.config import Config, DBConfig, MQConfig, get_config
from di.providers.context import AppContextProvider
from di.providers.db import DatabaseProvider
from di.providers.interactors import InteractorsProvider
from di.providers.repositories import RepositoriesProvider


def get_container() -> AsyncContainer:
    config = get_config()

    container = make_async_container(
        AppContextProvider(),
        FastapiProvider(),
        DatabaseProvider(),
        RepositoriesProvider(),
        InteractorsProvider(),
        context={
            Config: config,
            DBConfig: config.db_config,
            MQConfig: config.mq_config,
        },
    )
    return container
