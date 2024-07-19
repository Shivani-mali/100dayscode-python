# STRING METHODS:-2
a = "Shivani Mali[The Programmer]"
print(len(a))
print(a.upper()) #STRINGS ARE IMMUTABLE.:-NOT CHANGES...
print(a.lower()) 

# All abot the rstrip():-
a = "Shivani!!!!!!!"
print(len(a))
print(a)
print(a.upper()) #STRINGS ARE IMMUTABLE.
print(a.lower()) 
# print(a.rstrip("!"))it's remove the !! sign..

# All about the replace():-
# THe replace() method replaces all occrunce of the string with the another string!
# example:-
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
print(a.replace("Shivani", "Nilam"))

# All about the Split():-
# This mrthod splits the given string at the specified instance & return the separated string as list iteams.
# For example:-
print(a.split(" "))

#All about the Capitalize():-is used for the blog writing..
# For example:-
n = "hello"
capn = n.capitalize()
print(capn)
n1 = "heLlo World"
capn1 = n1.capitalize()
print(capn1)  #it automatically repair all the charectors!!

#All abot the center():-
# for example:-
h = "welcome to console!!!"
print(len(h))
print(h.center(50))

#All about the count():-
# for example:-
k = "Abbadabajaba"
countk = k.count("a")
print(countk)

#All about the endswitch():-
# for example:-
str4 = "Welcome to the console  !!!"
print(str4.endswith("!!!"))  #it's given the data as Boolean Data!!
print(str4.endswith("to", 4, 10))  #it's given the data as Boolean Data!!

# All about the find():-
# for example:-
f = "He's name is Dan. He is an honest man."
print(f.find("is")) #it's given the first occurance by the number!!

# All about the index():-
# For example:-it show error when give wrong.so it's raise the exception:-
d = "He's name is Dan. He is an honest man."
print(f.index("Dan"))
# it gives us the position!!!!!!!!!

# All about the isalnum():-
# For example:-
str1 = "WelcomeToTheConsole"
print(str1.isalnum())


# All about the isalpha():-
# for example:-
str7 = "Welcome"
print(str7.isalpha())
# all is in lower or wrong then it's return value is False
f= "Jungle main SHERR"
print(f.isalpha())

# All about the isprintable():-
# For ex:-
str0 = "hey anna\n"
print(str0.isprintable()) #its give false because the given string is not contain the right..

# All aboout the isspeace():-
# for example:-
o = "       " #using spacebar.
print(o.isspace())
o1 = "  "#using tab
print(o1.isspace())

# All aboout the istitle():-
# for example:-
i = "satya is a ceo of microsoft"
print(i.istitle())
p= "My Life Is Reading"
print(p.istitle())
p = "I AM THE BEST"
print(p.istitle())

# All about the isupper():- It is opposite to the istitle()
i = "I AM THE BEST"
print(i.isupper())

# All about the startswitch():-
strp = "Python is a objective Learning Language"
print(strp.startswith("Python"))
print(strp.startswith("is"))

# All about the swapcase():-
strp = "Python is a objective Learning Language"
print(strp.swapcase())
# its make the uppercase into lower and the lower case into upper..

# # All about the title():-
# For ex:-
n = "sri krishna is great"
print(n.title())

