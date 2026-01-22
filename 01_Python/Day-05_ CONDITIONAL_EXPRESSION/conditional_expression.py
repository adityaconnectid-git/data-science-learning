# Day 05  CONDITIONAL EXPRESSION

# if, else and elif
# If else and elif statements are a multiway decision taken by our program due to certain
# conditions in our code

# if and else ladder
age = int(input("Enter your age :"))
if(age>=18):
    print("You are above the age of consent")
    print("Good for you")
else:
    print("You are below the age of consent")

# if, elif and else ladder
age1 = int(input("Enter your age :"))
if(age1>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(age1<0):
    print("You are enter the invalide negataive age")
elif(age1==0):
    print("YOU are entering 0 which is not a valide age")
else:
    print("You are below the age of consent")

# Every if statment are run independely
age2 = int(input("Enter your age :"))
# If statement no.1
if(age2%2==0):
    print("Age2 is even")
# End of statement no.1
# If statement no.1
if(age2>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(age2<0):
    print("You are enter the invalide negataive age")
elif(age2==0):
    print("YOU are entering 0 which is not a valide age")
else:
    print("You are below the age of consent")
# End of statement no.1

# Queation

# 1. Write a program to find the greatest of four numbers entered by the user

a1 =int(input("Enter a number: "))
a2 =int(input("Enter a number: "))
a3 =int(input("Enter a number: "))
a4 =int(input("Enter a number: "))
if(a1>a2 and a1>a3 and a1>a4):
    print("Grater number is a1: ",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Grater number is a2: ",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Grater number is a3: ",a3)
else:
    print("Grater number is a4: ",a4)

# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

marks1= int(input("Enter marks 1: "))
marks2= int(input("Enter marks 2: "))
marks3= int(input("Enter marks 3: "))
# Check for total percentage
total_percentage= (100*(marks1 + marks2 + marks3)/300)
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass: ",total_percentage)
else:
    print("You are fail try to next year: ",total_percentage)
    
#3. A spam comment is defined as a text containing following keywords:
#“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
#to detect these spams.

p1 = "Male a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
massage = input("Enter your commont: ")
if((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("This commont is spam")
else:
    print("This is not a spam")

#4. Write a program to find whether a given username contains less than 10
#characters or not.

username = input("Enter your user name")
if(len(username)<10):
    print("This is valide ")
else:
    print("This is not vlaid enter min 10 digit")

# 5. Write a program to find out whether a given post is talking about “Jack” or not

post = input("Enter the post: ")
if("Jack".lower() in post.lower()):
    print("This post is talking about jack")
else:
    print("This post is not talking about jack")