# # operations on tuples in python :
# # its not directly manipluted

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

# you can change here the tuple but here the proces is to long!


# we merage here :
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
# here also this method we use for addding this method

# Syntax
# tuple.count(element)

# example:count()
#  Method :
# ===The count() method of Tuple returns the number of times the given element appears in the tuple.===
tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple.index(2)
res = tuple.index(3)
print('First occurrence of 2 is:', res)
print('First occurrence of 3 is:', res)

# ===The index():::The Index() method returns the first occurrence of the given element from the tuple.===
# Syntax:
# tuple.index(element, start, end)

tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple.index(3)
new = tuple.index(2)
print('First occurrence of 3 is', res)
print('First occurrence of 2 is', new)

# It's also do the slicing:
res = tuple.index(3, 4, 8)
print('count of 3 in tuple is:', res)

