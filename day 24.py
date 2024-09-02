# The new begainig of the 100 days of code in python with Harry!
#TUPLE:-
tup = (1, 5, 6)
print(type(tup), tup)  #always write(1,)
# is it changable.= 

print(tup[0])
print(tup[1])   #its give the values of tuple only seen their! 
print(tup[2])

# +ve and -ve indexing.
tup = (23, 4, 3, 12, 45, 65, 7, 8, "green", "orange")
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1]) #always starts from "0"
print(tup[2])

if 23 in tup:
    print("Yes it is present their") 
tup2 = tup[1:4]  #its print the position values!!
print(tup2)

# it is as similar as list : only you cant change the values of tuple!!