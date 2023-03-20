from loguru import logger


class BaseBrokerException(Exception):
    logger = logger

    def __init__(self, message: str):
        self.logger.exception(message)
        super().__init__(message)


class BrokerConnectionError(BaseBrokerException):
    pass


class UrlBrokerError(BaseBrokerException):
    pass


class ChannelBrokerError(BaseBrokerException):
    pass


class QueueBrokerError(BaseBrokerException):
    pass


class RoutingKeyBrokerError(BaseBrokerException):
    pass
