# Sets method ::::::::::Joining Sets:::::::::
# I. union() and update():
s = {1, 2, 5, 6}
s2 = {3, 4, 6, 7}
print(s.union(s2))
s.update(s2)    #update values which can u add
print(s, s2)
# again number is not repeated

# II. intersection and intersection_update():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3) #values in both set print here or update
# The intersection() method returns a new set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities) 
 #values are updated /// Or the original value is updated
#  intersection_update() method updates into the existing set from another set.

# III. symmetric_difference and symmetric_difference_update():
# prints only items that are not similar to both the sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# symmetric_difference_update()
#  method updates into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

# IV. difference() and difference_update():
# The difference() method returns a new set .
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

# whereas difference_update() method updates into the existing set from another set.
#  difference_update():::+++
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))


# isdisjoint():
# The isdisjoint() method checks if items of given set are present in another set.
#  This method returns False if items are present, else it returns True.
nilam = {25, 9, 2005}
aishu = {25, 1, 2005}
print(nilam.issubset(aishu))
# Same value then answer false

# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. 
# It returns True if all the items are present, else it returns False.
shiva = {"nilam", "satty","happy"}
shivi = {"nilam", "satty"}
print(shiva.issuperset(shivi))
# they "Shivi" element is present in the values of "Shiva"
# present = true or /// False

# issubset():
# The issubset() method checks if all the items of the original set are present in the particular set.
# It returns True if all the items are present, else it returns False.
shiva = {"nilam", "satty","happy"}
shivi = {"nilam", "satty"}
print(shivi.issubset(shiva))

# add()
# If you want to add a single item to the set use the add() method
love = {"Tokyo", "Madrid", "Berlin", "Delhi"}
love.add("Helsinki")
print(love)

# remove()/discard()
# We can use remove() and discard() methods to remove items form list.
alex = {"my", "life", "is", "BAdass", "Great"}
alex.remove("BAdass")
alex.discard("badass") #use discard it not show error
print(alex)

# pop()
# random value is pop & can you pop
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)
# value out and show you

# del
# del is not a method, rather it is a keyword which deletes the set entirely.
lifetruth= {"trust", "faith", "spiritual", "attitude", "thaughts", "gratitude"}
life = {"don't mind it", "not good"}
del life
# print(life) #show error because we delated
print(lifetruth)

# clear():
# This method clears all items in the set and prints an empty set.
lifetruth= {"trust", "faith", "spiritual", "attitude", "thaughts", "gratitude"}
lifetruth.clear()
print(lifetruth)
