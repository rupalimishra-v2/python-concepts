""" List Slicing """
new_list = ['a', 'b', 'c']
print(new_list[1])
# b

print(new_list[-2])
# b

print(new_list[1:3])
# ['b', 'c']

new_list[0] = 'z'
print(new_list)
# ['z', 'b', 'c']

my_list = [1, 2, 3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
# ['z', 2, 3]

print(bonus)
# [1, 2, 3, 5]

""" Matrix"""
# using this list:  access "Oranges" and print it
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
print(basket[1][1][0])

""" List Exercise """
# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list
basket.remove('Banana')

# 2. Remove "Blueberries" from the list.
basket.pop()

# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')

# 4. Add "Apples" at the beginning of the list
basket.insert(0, 'Apples')

# 5. Count how many apples in the basket
basket.count('Apples')

# 6. empty the basket
basket.clear()


""" Common list patterns """
#fix this code so that it prints a sorted list of all of our friends (alphabetical).
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

print(friends.sort() + new_friend)

#Solution
# friends.extend(new_friend)
# print(sorted(friends))