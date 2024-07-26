# # # LISTS:- It can be change!
# l = [3, 5, 6]
# print(l)
# print(type(l))

# Also we can here use:- seprated by "," and close by "[]"
# marks = [3, 5, 6]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])



# #List Index:-
# #  List Index
# # Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

# # Example:
# # colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# # #          [0]      [1]     [2]      [3]      [4]
# # Accessing list items
# # We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...

# # Positive Indexing:
# # As we have seen that list items have index, as such we can access items using these indexes.

# # Example:
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [0]      [1]     [2]      [3]      [4]
# print(colors[2])
# print(colors[4])
# print(colors[0])

# # Negative Indexing:
# # Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

# # Example:
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])

# We can add here string and bullean data:
marks = [3, 5, 6, "Shivi", True, 678, 90, "Life"]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

# Also:-
print(marks[-3]) #Negative index
print(marks[len(marks)-3]) #Positive index
print(marks[5-3]) #Positive index
print(marks[2]) #Positive index

if "Shivi" in marks:
    print("yes")
else:
    print("no")

# Same things are appilacable for string.
# if "Ha" in "Harry"
# print("yes")

print(marks[0:5])
print(marks[1:7])
print(marks[1:7:3])


# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:
# List = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.

# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

# Condition: Condition checks if the item should be added to the new list or not.

# Example 1: Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
