#!/usr/bin/python3

import datetime
from functools import wraps


def parameter_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print("[%s] '%s' args: %s, kwargs: %s" % (timestamp, func.__name__, args, kwargs))
        return func(*args, **kwargs)

    return wrapper


@parameter_logger
def worker(delay_time):
    pass

if __name__ == "__main__":
    worker(5)
