from typing import AsyncIterable
from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

from core.config import DBConfig
from domain.interfaces.uow import IUOW
from infrastructure.uow import UOW


class DatabaseProvider(Provider):
    scope = Scope.REQUEST

    uow = provide(UOW, provides=IUOW)

    @provide(scope=Scope.APP)
    def get_engine(self, db_config: DBConfig) -> AsyncEngine:
        return create_async_engine(url=db_config.uri())

    @provide
    def get_session_maker(
        self,
        engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        async_session = async_sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False,
            class_=AsyncSession,
            expire_on_commit=True,
        )
        return async_session

    @provide
    async def get_session(
        self,
        async_session: async_sessionmaker[AsyncSession],
    ) -> AsyncIterable[AsyncSession]:
        async with async_session() as session:
            yield session
