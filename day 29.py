# Doc - String:
# DOC-STRING AND Pep-string:
# For knowing the function is it used!

def square(n):
  print(n) #it is become none!
  '''Takes in a number n, returns the square of n'''
  print(n**2)
  print(n**3)
square(5)
print(square.__doc__)
 #the doc string is not ignore after function body add the string !

 
# Python Comments
# Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

# Python docstrings
# As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

# We can access these docstrings using the doc attribute.

# Python doc attribute
# Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring.

# Example
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
print(square.__doc__)

# pepit is it used for the: "Python enhancement proposal"
# EAster eggs
# PS C:\Users\DELL> python
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import this
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# >>>