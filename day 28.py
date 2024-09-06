# f - strings:
# USE FOR USING VARIABLES!
# String formating use their
letter = "hey my name is {} and i am from {}"
country = "India"
name = "Shiva"

print(letter.format(name, country))

# A new exaple
letter = "I am the {0} Student, I like {1}"
coursename = "CSE"
hobby = "Programming"

print(letter.format(coursename, hobby))


# but it is to long so, here we use abstract:=
print(f"hey my name is {name} and i am from {country}")
country = "India"
name = "Shiva"

new = "I am the {} person of my {}"
fav = "favourite"
solumate = "Wife"
print(f"I am the {fav} person of my {solumate}")

# how we can use this for maths:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.0000))

price = 49.00099
txt = f"For only {price:.2f}"
print(txt)

# Also it is used as!
print(f"{2*34}")
# we also used this as string for finding values!!


#  How i use the f-string!
print(f"hey my name is {{name}} and i am from {{country}}")
# As it this value give it's give my return value!