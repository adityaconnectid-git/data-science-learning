# Day 03 Lists and Tuple

# List
friends = ["Apple", "Mango", "Roahn", 25 ,35.54]
print(friends[0])
friends[0]= "Papaya" # Unlike String list are mutable
print(friends[0]) # It is print first element
print(friends[0:3])
print(friends[0:4:2])

# List Methods
friends.append("Monkey") # It is add at the end 
print(friends)
l1 = [1,8,7,2,21,15]
l1.sort() # It is short the given list
print(l1)
l1.reverse() # it is print the reverse list
print(l1)
friends.insert(2, 22) # It is insert the value on the place of given index
print(friends)
value= l1.pop(3) # It is remove the value at givem index
print(value)
print(l1) 
l1.remove(1) # It is remove the perticular value
print(l1)

# Tuple 
# A tuple is an immutable data type in python.
a = () # empty tuple
print(type(a))
b = (1,) # tuple with only one element needs a comma
print(type(b))
c = (1,7,2, "Rohan" , "Sumit" , False ,2 , 5, 2) # tuple with more than one element
print(type(c))
print(c)

# Tuple Method
no = c.count(2) # It is count how many time the given number is present
print(no) 
i = c.index(2) # it is find the fisrt index of given vakue 
print(i)

# Question
# Q1. Write a program to sum a list with 4 numbers
l=[11,22,33]
print(sum(l)) # sum function is add all the list