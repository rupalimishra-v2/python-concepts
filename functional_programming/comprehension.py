""" List comprehension: It's a way for us to quickly create lists with Python instead of looping and using append
# or things that we've seen before. """

# Way 1
my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)

# Way 2 - comprehension
my_list_1 = [char for char in 'hello']
print(my_list_1)

# Example 2
my_list_2 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(my_list_2)

""" Set comprehension: It's a way for us to quickly create sets with Python instead of looping and using append
# or things that we've seen before. """

# Way 1
my_set = []
for char in 'hello':
    my_set.append(char)
print(my_set)

# Way 2 - comprehension
my_set_1 = {char for char in 'hello'}
print(my_set_1)

# Example 2
my_set_2 = {num ** 2 for num in range(0, 100) if num % 2 == 0}
print(my_set_2)

""" Dictionary comprehension: It's a way for us to quickly create dictonaries with Python instead of looping and using
 append or things that we've seen before. """

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)


# Exercisethe : Remove duplicates from list using comprehension

my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Traditional method
duplicates = []
for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
print(duplicates)

# Comprehension Method
duple = list({i for i in my_list if my_list.count(i) > 1})
print(duple)

