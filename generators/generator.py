""" Calculate the performance or time taken to complete a function.
# Every generator is an iterator, example - range
# Every iterator is not a generator , example - list

How to create a generator function :
def gen_fun():
    for num in range(100):
        yield num

yield basically pause the function and it's result can be used later on."""
from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        before = time()
        func(*args, **kwargs)
        after = time()
        print(f'Took {after - before}ms')
        return None

    return wrap_func


# Took 2.7973110675811768ms - because it does not have to hold everything in memory
@performance
def long_time():
    for iterator in range(100000000):
        iterator * 2

# Took 6.095685005187988ms
@performance
def long_time_without_generator():
    for iterator in list(range(100000000)):
        iterator * 2


long_time()
long_time_without_generator()
