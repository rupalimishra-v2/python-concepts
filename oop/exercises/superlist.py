#Create a superlist that on asking length always return 1000 and has all the functionality of list.
# Notice that Superlist is extending list class as parent class to inherit it's functionality and then contains the
# __len__ dunder method to meet our requirement.
class SuperList(list):
  def __len__(self):
    return 1000

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(list, object))