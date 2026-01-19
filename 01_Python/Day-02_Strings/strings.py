# Day 2: Python Strings

# Strings
name = "Ram Roy"
print(name)

# String Slicing
shortname = name[0:2]# start from 0 all way the till 2(excluding 2)
print(shortname)
print(name[-3:-1]) # Negative slicing
print(name[4:6]) # Change negative into positive
character1 = name[1]
print(character1)
print(name[:4]) # It is starting from 0 and goes to 4 
print(name[1:]) # It is start from 1 and goes to the last 
print(name[0:7:2]) # Slicing with Skip value

# String Function
print(len(name)) # It is write the lenght of the string
print(name.endswith("roy")) #It is check it is end with this or not
print(name.startswith("R")) #It is check it is start with this or not
count = name.count("R")
print(count) # It is count who many time it is present in this string
str = "rohit tiwari"
capitalized_string = str.capitalize()
print(capitalized_string) # It is captail the first latter of string
replaced_string = name.replace("a", "o")
print(replaced_string) # It it is use to replace any word
index = name.find("m")
print(index) # It is use to find the index of given vakue