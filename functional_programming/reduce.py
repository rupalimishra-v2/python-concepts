from functools import reduce

# 4 Combine all of the numbers that are in a list using reduce (my_numbers and scores). What is the total?
my_numbers = [5, 4, 3, 2, 1]
scores = [73, 20, 65, 19, 76, 100, 88]


def red(acc, item):
    return acc + item


print(reduce(red, scores, reduce(red, my_numbers, 0)))
