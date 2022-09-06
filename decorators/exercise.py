# Calculate the performance or time taken to complete a function.
from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        before = time()
        func(*args, **kwargs)
        after = time()
        print(f'Took {after - before}ms')
        return None

    return wrap_func


@performance
def long_time():
    for iterator in range(1000):
        iterator * 2


long_time()