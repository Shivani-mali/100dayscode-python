# LIST METHODS:- they are many types!

l =[43, 56, 1, 3, 5, 45]
print(l)
# l.append(90)   #it's add the numgber
l.sort()          #its gives the data within the number
print(l)
l.sort(reverse=True)       #its give in desending order
print(l)
l.reverse()    #main list make opposite
print(l)

print(l.index(3))  #it showcase the values.
print(l)
# print(l.index(1))  *its first accourance is index
print(l)

print(l.count(1)) #HOW many times number is present.
print(l)

# copy method 
m =l        #you change the list by copy method
m[0] = 0
print(m)

l.insert(1, 899) #add the value
print(l)

m = [900, 970, 1100]   #its do a work as Extend and insert
l.extend(m)
print(m)


n = [900, 970, 1100, 788]   
k = l + n 
print(k)


