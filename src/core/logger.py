from logging import (
    DEBUG,
    getLogger,
    Logger,
    StreamHandler,
    FileHandler,
    Formatter,
)


def get_logger() -> Logger:
    logger = getLogger("app")

    log_format = (
        "%(asctime)s - [%(levelname)s] - %(name)s - "
        "(%(filename)s:%(lineno)d) - %(message)s"
    )
    formatter = Formatter(log_format)

    stream_handler = StreamHandler()
    file_handler = FileHandler("app.log")

    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    logger.setLevel(DEBUG)

    return logger


logger = get_logger()
