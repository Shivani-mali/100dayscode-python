# # IF - ELSE CONDITIONAL:-
# Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. 
# If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

# Based on this, the conditional statements are further classified into following types:

# if
# if-else
# if-else-elif
# nested if-else-elif.
# An if……else statement evaluates like this:
# if the expression evaluates True:
# Execute the block of code inside if statement. After execution return to the code out of the if……else block.\

# if the expression evaluates False:
# Execute the block of code inside else statement. After execution return to the code out of the if……else block.

a = int(input("Enter your age"))
print("Your age is: ",a)
# Conditionsl operstors:-
# <,>,>=,<=,==,!
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)

if(a>18):
    print("You can drive")
    print("Yes")
else:
    print("you can not drive") #space is called as intendation!!!
    print("Not")
    print("Yay!")


applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart. ")
else:
    print("Alexa, do not add Apples to the cart.")


num = int(input("Enter the valus of num:"))
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")  

#For example my life...
str1 = (input("Enter name of your bestfriend: "))
if (str1 == "Shrutika"):
    print("She is not your friend!!")
elif (str1 == "Nilam"):
    print("She is your First best-friend: ")
else:
    print("You think About your past is wrong:-") 


#Nested IF statements:-
num = int(input("Enter the number:")) #also , for the specific number you can write their as #num = (number what you want!)
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")      

# That is all aboout the if else statement!!!!
