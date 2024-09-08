# Recursion:
# it is basically function but the work is here done is "Recall agagin and again"
# a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

# FActorial(7): 7*6*5*4*3*2*1
# FActorial(6): 6*5*4*3*2*1
# FActorial(0): 1
# Factorial(n) == n * factorial(n-1)

def factorial(num): 
    if (num == 0 or num == 1):
        return 1
    else:
        return (num * factorial(num - 1)) 
    
print(factorial(5))
print(factorial(2))    
print(factorial(3))    

  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))

# Also the exaple of fibnochi series given the example of recursion!