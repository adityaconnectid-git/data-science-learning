# Day 07 - Function and Recursions
# Tpoic: Function and Recursions

# Example 1: Average of the number
def avg():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))
    average = (a+b+c)/3
    print(average)

# Function call
avg()

# Function with Arguments
# Example 2: Great goood
def goodDay(name , ending="Thanks"):
    print("Good Day, "+name)
    print(ending)
    return "ok"
a = goodDay("Rohan", "Thank you")
print(a)
goodDay("Mohit")

def greet(name):
    gr = "hello "+ name
    return gr
a = greet ("Komal")
print(a)

# Recursion
# Example 3: Factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    return n * fact(n-1)
n = int(input("Enter the number: "))
print(f"The factorial of this number is : {fact(n)}")

# Example 4: Find the greatest number
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a = 5
b = 8
c = 1
print(greatest(a, b, c))

# Example 5: convert Celsius to Fahrenheit
def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter temperature in f: "))
c = f_to_c(f)
print(f"{round(c,2) } °C")

# Example 6: Calclute the first N natural number
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4))

# Example 7: Pattern
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
pattern(5)

# Example 8: Write a python function to remove a given word from a list ad strip it at the same
# time.
def rem(l, word):
    n =[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l = ["Apple", "Rohan", "Mango", "an"]
print(rem(l , "an"))

# Example 9: Printing the tables
def print_table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
print_table(5)