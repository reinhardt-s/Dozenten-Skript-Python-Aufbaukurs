from enum import Enum


class LogLevel(Enum):
    DEBUG = 3
    INFO = 2
    PRODUCTION = 1


LOG_LEVEL = LogLevel.INFO.value


class Logger:
    def debug(self, message):
        if LOG_LEVEL >= LogLevel.DEBUG.value:
            print(f'DEBUG:\t{message}')

    def info(self, message):
        if LOG_LEVEL >= LogLevel.INFO.value:
            print(f'INFO:\t{message}')

    def production(self, message):
        if LOG_LEVEL >= LogLevel.PRODUCTION.value:
            print(f'PRODUCTION:\t{message}')


log = Logger()
