# For Loops in Python:-
# Introduction to Loops
# Sometimes a programmer wants to execute a group of statements a certain number of times.This can be done using loops.
#  Based on this loops are further classified into following main types;

# 1) for loop. :- Dedicates to MEGA PROJECTS!!
#2) while loop.

# The "for loop":-for loops can iterate over a sequence of iterable objects in python. 
# Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
# For ex:- Itering over the string.

name = 'Shivali'
for i in name:
    print(i, end=" , ")

# orrrr
name = 'Shivali'
for i in name:
    print(i)    

k = 'Aai'
for i in k:
    print(i)
    if(i == "a"):
        print("This is the one letter of my world!!")


#List :-
colors = ["Red", "Yellow", "Black", "Blue"]
for color in colors:
    print(color)
    # Also write as:
    for i in color:
        print(i)


for k in range(5):
    print(k + 1)

for k in range(1 , 9):
    print(k + 1)

for k in range(1 , 50):
    print(k)

Table = int(input("Enter the number :")) #I make the table calculating value:-
for k in range(1 , 11): #Here put the eleven because the step back valuse is printes!!
    print(k * Table)

# # For the 3 arguments what is the ans??
for k in range (1, 15, 66):
    print(k)



