from dataclasses import dataclass, field
from tomllib import load


@dataclass
class DBConfig:
    username: str
    password: str
    host: str
    name: str
    port: str
    driver: str = field(default="postgresql+psycopg")

    def uri(self) -> str:
        return (
            f"{self.driver}://{self.username}:{self.password}@"
            f"{self.host}:{self.port}/{self.name}"
        )


@dataclass
class MQConfig:
    username: str
    password: str
    host: str
    port: int

    def uri(self) -> str:
        return f"{self.host}:{self.port}"


@dataclass
class Config:
    db_config: DBConfig
    mq_config: MQConfig


def get_config(filename: str = "configuration.toml") -> Config:
    with open(filename, "rb+") as config_toml:
        data = load(config_toml)

    config = Config(
        db_config=DBConfig(
            username=data["db"]["username"],
            password=data["db"]["password"],
            host=data["db"]["host"],
            port=data["db"]["port"],
            name=data["db"]["name"],
        ),
        mq_config=MQConfig(
            username=data["mq"]["username"],
            password=data["mq"]["password"],
            host=data["mq"]["host"],
            port=data["mq"]["port"],
        ),
    )
    return config
