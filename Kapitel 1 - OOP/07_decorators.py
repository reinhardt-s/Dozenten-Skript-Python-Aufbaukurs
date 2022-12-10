# @abstractmethod
import locale

from datetime import datetime, timedelta
from functools import wraps

locale.setlocale(locale.LC_ALL, locale='de')


def decorator_mit_wrapper(func):
    def wrapper():
        print('Vor dem Funktionsaufruf')
        result = func()
        print('Nach dem Funktionsaufruf')
        return result

    return wrapper


def time_converter(func):
    def wrapper():
        result = func()
        result = result.strftime("%A der %d. %B %Y")
        return result

    return wrapper


def to_local_time(lang='de'):
    def decorator(func):
        def wrapper():
            result = func()
            locale.setlocale(locale.LC_ALL, locale=lang)
            result = result.strftime("%A, %d. %B %Y")
            locale.setlocale(locale.LC_ALL, locale='de')
            return result

        return wrapper

    return decorator


def plan_ahead(func):
    def wrapper(*args, **kwargs):
        print(kwargs)
        print(*args)
        if 'plus_days' in kwargs:
            print(f'Das Ereignis liegt {kwargs["plus_days"]} Tage(e) in der Zukunft.')
        else:
            print(f'Das Ereignis liegt {args[0]}  Tage(e) in der Zukunft.')
        return func(*args, **kwargs)

    return wrapper


def to_local_time_2_0(lang='de'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            locale.setlocale(locale.LC_ALL, locale=lang)
            result = result.strftime("%A, %d. %B %Y")
            locale.setlocale(locale.LC_ALL, locale='de')
            return result

        return wrapper

    return decorator


# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
#
# @decorator_mit_wrapper
# @time_converter
@to_local_time(lang='de')
def show_date():
    return datetime.now()


@plan_ahead
@to_local_time_2_0(lang='fr')
def future_date(plus_days: int):
    return datetime.now() + timedelta(days=plus_days)


print(show_date())
print(future_date(plus_days=7))

print(future_date.__name__)
# @wraps(wrapped=func)
