# Functions in Python:-
# There are two types of functions:

# Built-in functions
# User-defined functions

# Built-in functions:
# These functions are defined and pre-coded in python. 
# Some examples of built-in functions are as follows:

# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

# Syntax:
# def function_name(parameters):
#   pass
 
# Code and Statements
def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)
a = 9
b = 8
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculateGmean(a, b)
c = 8
d = 7
# # gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c, d)
  


# find the freater number:-
def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass              #it states that "this function i write later!"
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)




