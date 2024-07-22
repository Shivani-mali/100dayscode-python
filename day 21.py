# Function arguments in Python:-Used for quote separation
# THEY ARE MAINLY 4 TYPES.
# Default arguments, keyword arguments, variable length arguments, Required arguments.

def average(a, b):
    print("The average is ", (a+b)/2)

average(4, 6)

# Default Arguments:-
# We can provide a default value while creating a function.
# This way the function assumes a default value even if a value is not provided in the function call for that argument.
def name(fname, mname = "Jhon", lname = "Whatson" ):
    print("Hello,", fname, mname, lname)

name("Amy", "Agrawal")


# Keyword arguments:
# We can provide arguments with key = value,
#  this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

def average(a= 9, b=34):
    print("The average is ", (a+b)/2)

# average(4, 6)
average(b=9)

average(b=9, a=21)


# Required arguments:
# In case we don’t pass the arguments with a key = value syntax, 
# then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition. 
# Example 1: when number of arguments passed does not match to the actual function definition.
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")
#DETECTED AS A ERROR......

# Example 2: when number of arguments passed matches to the actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Ego", "Quill")




# Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
def name(*name): #nAME IS CONSIDER AS A DICTIONARY!!!!!
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")
# There are two ways to achieve this:

# Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

# Example:
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")


f = average(9, 34)
print(f)





