# Dictionaires Method :
ep = {122: 45, 123: 89, 567:69, 670: 69}
ep2 = {222: 67, 566: 90}

ep.update(ep2)
print(ep)
# in python dictionary is ordere

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

# clear () & the Pop() Method !
ep.clear()
print(ep)
empt = {}
print(empt)

# popitem():
# The popitem() method removes the last key-value pair from the dictionary.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

