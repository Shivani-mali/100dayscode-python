# Exercise 2:-
# Good Morning Sir:-
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening.
#  Your program should use time module to get the current hour.
#  Here is a sample program and documentation link for you:
import time
t = time.strftime('%H:%M:%S')
print(t)
ṭ= int(time.strftime('%H'))
print(t)
t = int(time.strftime('%M'))
print(t)
t = int(time.strftime('%S'))
print(t)

if (t > 12):
    print("Good morning sir")
elif (t <= 12):
    print("Good afternoon sir")
elif (t > 17):
    print("Good evening sir")   
else:  
    print("IT IS A NIGHT TIME!!")  

#MY SOLUTION IS WRITE OR WRONG?? YOU HAVE THE ANSWER THEN ENROLL IT!!
         