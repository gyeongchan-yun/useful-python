#!/usr/bin/python3

import time


def measure_runtime(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()

        print("'%s' function running time: %s" % (func.__name__, end - start))
        return ret

    return wrapper


@measure_runtime
def worker(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    worker(5)
