from .log import log


def notified(function):
    def wrapper(*args, **kwargs):
        log.debug(f"{function.__qualname__} wurde vom Subject aufgerufen")
    return wrapper
