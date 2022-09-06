""" According to functional programming paradigm
- same data will always generate same result
- map function does not affect the outside world """

# 1 Multiply elements in data and print the list
data = [1, 2, 3, 4]


def multiply_by_3(item):
    return item * 3


print(list(map(multiply_by_3, data)))
print(data)


# 2 Capitalize all of the pet names and print the list
def capital(item):
    return item.upper()


my_pets = ['aiai', 'bibi', 'cici', 'didithe the ']
print(list(map(capital, my_pets)))
