# Day 04  DICTIONARY & SETS

# Dictionary
# Dictionary is a collection of keys-value pairs.
d= {} # It is a empty Dictionary
print(type(d))
marks = {
    "Rohan": 23,
    "Aman": 95,
    "Komal": 88, 
    "Arpit": 79
}
print(marks , type(marks))
print(marks["Aman"]) # It is print the value of given key
marks["Aman"]=98 # It is update the value of given key
print(marks)

# DICTIONARY METHODS
print(marks.items()) # It is give the key value pairs in the form of tuple
print(marks.keys()) # It is print all the key of the dictionary
print(marks.values()) # It is print all the value of the dictionary
marks.update({"Rohan":55, "Anshu":98}) # It is update the dictionary
print(marks)
print(marks.get("Ayush")) # It is return the none 
print(marks["Ayush"]) # It is return the error
print(marks.pop("Anshu")) # It is delete the given key and value
print(marks)
print(marks.popitem()) # It is remove and returns a key value pair. Pairs are returned in LIFO order
print(marks)
print(len(marks)) # It is print the length of the dictionary

# Sets
# Set is a collection of non-repetitive elements and it is not in order.
s= set() # It is print a empty set
print(type(s)) 
sett= {5,3,6,5,2,9,0,1,"Hello","Rohan",7.9}
print(sett)

# Set methods
sett.add(56) # It is add the value
print(sett)
sett.remove(0) # Itis remove the given element
print(sett)
sett.pop() # It is remove the random value from set
print(sett)
sett.clear() # It is clear all the set
print(sett)
s1 = {1,2,3,3,4,2}
s2 = {2,7,8,9,0,5,6}
print(s1.union(s2)) # It is print the union value 
print(s1.difference(s2)) # It is print the difference
print(s1.intersection(s2)) # It is print the common value
print(s1-s2) # It is print the difference
print(s2-s1)
print({1,2}.issubset(s1)) # It is print the subset

# Question
# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
words={
    "hathi": "elephant",
    "aam": "mango",
    "madad": "help" 
}
n=input("enter rhe word: ")
print(words[n])

# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once)
s3 = set()
m = input("Enter number")
s3.add(int(m))
m = input("Enter number")
s3.add(int(m))
m = input("Enter number")
s3.add(int(m))
m = input("Enter number")
s3.add(int(m))
m = input("Enter number")
s3.add(int(m))
m = input("Enter number")
s3.add(int(m))
m = input("Enter number")
s3.add(int(m))
m = input("Enter number")
s3.add(int(m))
print(s3)

# 3. What will be the length of following set s:
s4 = set()
s4.add(20)
s4.add(20.0)
s4.add('20') # length of s after these operations? 
print(len(s4)) # Because of if value is same then python is ignor the datatype
print(s4)

# 5. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
di = {}
name = input("Enter friends name")
lan = input("Enter their language")
di.update({name:lan})
name = input("Enter friends name")
lan = input("Enter their language")
di.update({name:lan})
name = input("Enter friends name")
lan = input("Enter their language")
di.update({name:lan})
name = input("Enter friends name")
lan = input("Enter their language")
di.update({name:lan})
print(di)