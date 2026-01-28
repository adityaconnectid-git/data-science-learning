# Day 11- Advance Topic
# Topic: Exception handling (basic)
#        List comprehensions
#        Enumerate
#        Lambda
#        Map & Filter

# Exception Handling
# try – except Block
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Division by zero not allowed")

# Common Built-in Exceptions
# (a) ZeroDivisionError
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
# (b) ValueError
try:
    x = int("abc")
except ValueError:
    print("Invalid value")
# (c) TypeError
try:
    print(10 + "5")
except TypeError:
    print("Type mismatch")
# (d) IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range")
# (e) KeyError
try:
    d = {"name": "Aditya"}
    print(d["age"])
except KeyError:
    print("Key not found")
# (f) FileNotFoundError
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")

# Multiple except Blocks
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Enter only numbers")
except ZeroDivisionError:
    print("Zero is not allowed")

# Exception as e
try:
    x = int("abc")
except Exception as e:
    print("Error:", e)

# else Block
try:
    x = int(input("Enter number: "))
    y = 10 / x
except ZeroDivisionError:
    print("Zero error")
else:
    print("Result:", y)

# finally Block
try:
    file = open("data.txt")
    print(file.read())
except FileNotFoundError:
    print("File missing")
finally:
    print("Program finished")

# raise Keyword
age = int(input("Enter age: "))

if age < 18:
    raise ValueError("Age must be 18 or above")

# User-Defined (Custom) Exception
class NegativeNumberError(Exception):
    pass

try:
    n = int(input("Enter number: "))
    if n < 0:
        raise NegativeNumberError("Negative number not allowed")
except NegativeNumberError as e:
    print(e)

# Enumerate Function
l = [2, 523, 78, 45, 34]
# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1
# This is simplified using Enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

# List comprehensions
myList = [1, 3, 5, 7, 9]
# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

## Using list comprehensions
squaredList = [i*i for i in myList]
print(squaredList)

# Write a program to print third, fifth and seventh element from a list using enumerate
# function.
myList = [1, 3, 5, 7, 9, 15, 2]
for i, item in enumerate(myList):
    if i == 2 or i == 4 or i == 6:
        print(item)

#Write a list comprehension to print a list which contains the multiplication table of a
#user entered number.
n = int(input("Enter a number: "))
table = [n*i for i in range(1,11)]
print(table)

# Store the multiplication tables generated in upper question in a file named Tables.txt
n = int(input("Enter a number: "))
table = [n*i for i in range(1,11)]
with open("table.txt","a") as f:
    f.write(f"Table of {n}: {str(table)}\n")

# Lambda function
def square(n):
    return n*n

square = lambda x:x*x 
print(square(6))
sum = lambda a,b,c:a+b+c 
print(sum(1,2,3))

## Map & Filter
l = [1, 4, 6, 8, 33, 76]
square = lambda x:x*x 
sqList =map(square, l)
print(list(sqList))

def even(n):
    if (n%2==0):
        return True
    return False
onlyEven = filter(even, l)
print(list(onlyEven))