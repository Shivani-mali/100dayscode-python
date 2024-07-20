# Break and continue statement:-
for i in range(12):
    if(i == 10):
     break
    print(" 5 X", i+1 , "=", 5 * (i+1))
    

print("Loop ko chor kr nikal gaya")



for i in range(12):
    if(i == 10):
     print("Skip  the iteration!!")
     continue
    print(" 5 X", i+1 , "=", 5 * (i+1))
    
# WHILE TRUE:-us efor the do while loop:-
i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break

#Do while loop run :- one times! 
    
 