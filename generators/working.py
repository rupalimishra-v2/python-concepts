# Code your own for loop and range function

# For loop
def special_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

print(special_for_loop([1,2,3,4]))

# Range function
class MyGenerator:
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGenerator.current < self.last:
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        raise StopIteration

generator = MyGenerator(0,20)
for i in generator:
    print(i)