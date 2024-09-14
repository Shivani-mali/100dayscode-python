# Dictionairy
# Dictionaries are ordered collection of data items. 
# They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

dic ={
        "Shivani": "Human being",
        "Spoon": "Object"

}
print(dic["Shivani"]) 

# Use for the mapping 
dic ={

    34:"Naina",
    42:"rani",
    90:"Shubham"
}
print(dic[34])

# Accesing values:single
# Values in a dictionary can be accessed using keys.
#  We can access dictionary values by mentioning keys either in square brackets or by using get method.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info.keys())
print(info.values())  #you get the values


for key in info.keys():
    print(info[key])

# also we can write it 
for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}") 
  


print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  