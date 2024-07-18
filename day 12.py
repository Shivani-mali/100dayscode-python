#STRING METHODS:-
#STRING SLICING:-
names = "Shivani,Aishwarya"
# print(name[0:any number])
print(len(names)) #it's calculate the values of given string

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")#within the statement you canwrite the value
print(fruit[4])
print("I like this", len1, "Charectors")


#use for slicing[]this bracket!!
print(fruit[0:4])  #including 0 but not 4.
print(fruit[:4])
print(fruit[1:4])  #including 1 but not 4.
print(fruit[1:])   #python is totally a good because it auttomatically fill the data. 

# Now do some "Negative slicing"
print(fruit[0:-3]) #it goes towards backside because the "-" sign minus!!
print(fruit[0:len(fruit)-3]) #both are same
print(fruit[-1:len(fruit)-3])#it" not print?~~
print(fruit[-3:-1])

# LOOP THROUGH A STRING:-
# example
alphabates = "ABCDE"
for i in alphabates:
    print(i)


#QUICK QUIZ:-
nm = "HARRY"
print(nm[-4:-2])
new = "SHIVANI"
print(new[-7:-3])

