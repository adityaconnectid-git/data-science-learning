# Day 06 - loops
# Topic: • while loops and • for loops

# While loop
# Example 1: Print 1 to 50 using while loop
i=1
while(i<51):
    print(i)
    i+=1

# Example 2: Print "John" – 5 times!
i = 0
while i < 5: 
    print("John")
    i = i + 1

# Example 3: Print the content of a list using while loops.
l = [1,"Rohan",False,"Subham","Arpit"]
i=0
while(i<len(l)):
    print(l[i])
    i+=1

# For loop
# Example 4: Print the value 0 to 5
for i in range(6):
    print(i)

# Example 5: Print the content of a list using for loops.
l = [1, 7, 8]
for item in l:
    print(item)

# Example 6: Iterate the tuple using for loops.
t=(1,3,33,66,2,79,24,6)
for i in t:
    print(i)
 
# Example 7: Iterate the string using for loops.
s="Rohan"
for i in s:
    print(i)

# Example 8: For loop withs else
for i in range(6):
    print(i)
else:
    print("Done")

# Brack
# Example 9:
for i in range (0,80):
  print(i) 
  if (i==3):
   break

# Question
# Q1. Print given table
n = int(input("Enter the number: "))
i=0
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

# Q2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
for i in l:
    if i.startswith("S"):
        print(f"Hello {i}")

# Q3. Write a program to find whether a given number is prime or not.
n = int(input("Enter the number: "))
for i in range(2,n):
    if (n%i) == 0:
        print("Number is not prime ")
        break
else:
    print("Number is prime")

# Q4.  Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter the number: "))
i = 1
sum = 0
while (i<=n):
    sum = sum + i
    i +=1
print(sum)

# Q5. Write a program to calculate the factorial of a given number using for loop.
n = int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# Q6. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print(" ")

# Q7. * * *
#     *   * for n = 3
#     * * *
n = int(input("Enter the number: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")

# Q8. Write a program to print multiplication table of n using for loops in reversed
# order.
n = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} * {11-i} = {n*(11-i)}")