# Square
my_list = [5, 4, 3]


# Way 1
def square(item):
    return item ** 2


print(list(map(square, my_list)))

# Way 2
print(list(map(lambda item: item ** 2, my_list)))

# List sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
