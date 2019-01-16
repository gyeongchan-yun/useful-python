#!/usr/bin/python3

import os
import time
import psutil
from functools import wraps


def performance_check(func):
    process = psutil.Process(os.getpid())

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_mem = process.memory_info().rss
        start_cpu = process.cpu_percent(interval=0.0)

        start_t = time.time()
        ret = func(*args, **kwargs)
        end_t = time.time()

        end_mem = process.memory_info().rss
        end_cpu = process.cpu_percent(interval=0.0)

        runtime = end_t - start_t
        cpu = end_cpu - start_cpu
        mem = end_mem - start_mem

        return (cpu, mem, runtime, ret)

    return wrapper


@performance_check
def example_func(items):
    count = 0
    for item in items:
        count += 1
    return count


if __name__ == "__main__":
    cpu, mem, runtime, count = example_func(range(1000))
    print("[CPU Usage] %s" % cpu)
    print("[MEM Usage] %s" % mem)
    print("[Run Time] %s" % runtime)
    print("[Iteration count] %s" % count)
