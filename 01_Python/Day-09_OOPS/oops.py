# Day 09 - OOPS

# Example 1: Make a simple Class and Object
class Employee:
    language = "python" # this is class attributes
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def great():
        print("Good morning")

emp1 = Employee()
emp1.name = "Jack" # this is instance attributes
print(emp1.name,emp1.language,emp1.salary)

emp1.getInfo()
emp1.great()
Employee.getInfo(emp1)

emp2 = Employee()
emp2.name = "Mical"
emp2.language = "Java"
print(emp2.name,emp2.language, emp2.salary)
# Here name is instance arrtibute and salary and language are class
# attributes as they directely belong to the class

# Example 2: use INIT method
class Employee:
    language = "python" # this is class attribute
    salary = 120000


    def __init__(self, name , salary , language): # dunder method which is automatically called
        self.name = name 
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getinfo(self):
        print(f"the language is {self.language} . The salary is {self.salary}")

    @staticmethod
    def great():
        print("Good morning")
jack = Employee("Jack" , 1300000 , "Java")
jack.getinfo()
jack.great()
Employee.getinfo(jack)

# Example 3: Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self , name , salary , id):
        self.name = name 
        self.salary = salary
        self.id = id

p = Programmer("Aman" , 1200000 , 111)
print(p.name , p.company , p.salary , p.id)

q = Programmer("Rani" , 1200000 , 111)
print(q.name , q.company , q.salary , q.id)  

# Example 4: Write a class “Calculator” capable of finding square, cube and square root of a
# number.
class Calculator :
    def __init__(self ,n):
        self.n = n
    def square(self):
        print(f"The square of the number is {self.n*self.n}")
    def cube (self):
        print(f"The cube of the given number is {self.n*self.n*self.n}")
    def root (self):
        print(f"The cube of the given number is {self.n**0.5}")
    @staticmethod
    def hello():
        print("!heloo")

a = Calculator(5)
a.square()
a.cube()
a.root()
a.hello()

# Example 5: Create a class with a class attribute a; create an object from it and set ‘a’
#directly using ‘object.a = 0’. Does this change the class attribute?
class Demo :
    a=4
o= Demo()
print(o.a) #print the class attribute because inatance atteibute is not present 
o.a = 0 # instance attribute is set
print(o.a)# it is print the intance attribute is set
print(Demo.a)# it is print the class attribute

# Example 6: Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
#and get fare information of train running under Indian Railways
from random import randint

class Train:
    def __init__(self , trainno):
        self.trainno = trainno

    def book(self , fro , to):
        print(f"Ticket is booked in  train no {self.trainno} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no {self.trainno} is running on time")

    def getFair(self , fro , to):
        print(f"Ticket fair in the train no {self.trainno} from {fro} to {to} is {randint(222,555)}")

t = Train(125500)
t.book("Nihalghar " , "delhi")
t.getStatus()
t.getFair("Nihalghar " , "delhi")
