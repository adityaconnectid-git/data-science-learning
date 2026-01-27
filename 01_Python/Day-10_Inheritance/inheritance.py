# Day - Inheritance

# Example 1: Simple example of inheritance
class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

a = Employee()
print(a.name,a.company)

class Programmer (Employee ):
    company = "ICT Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

b = Programmer()
print(b.name , b.company)

# Example 2: Multi Inheritance
class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder :
    language = "Python"
    def printLanguage (self):
        print(f"Out of all the language here is your language : {self.language}")

class Programmer (Employee , Coder):
    company = "ICT Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()
print(a.company , b.company )

# Example 3: Multilavel inheritance
class Employee:
    a = 1

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 4

o = Employee()
print(o.a)
# print(o.b)  it show the error because b is not attribute of employee

o = Programmer()
print(o.a , o.b)
print(o.b)

o = Manager()
print(o.a , o.b , o.c)
print(o.b)
print(o.c)

# Example 4: Use super method
class employee:
    def __init__(self):
        print("Constructor of employee")
    a = 1

class Programmer(employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of manager")
    c = 4

o = manager ()
print(o.a , o.b , o.c)

# Example 5: Class method is use for directely use the class method 
class Employee():
    a = 1 

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()

# Example 6: There is use of property and setter method
class Employee():
    a = 1 

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self , value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Aditya Tiwari"
print(e.name , e.fname , e.lname)

e.show()

# Example 7: Method overloding 
# __str__() used to set what gets displayed upon calling str(obj)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} scored {self.marks}"

s = Student("Aman", 90)
print(s)

# __add__() – + operator
class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

v1 = Vector(10)
v2 = Vector(20)
print(v1 + v2)

# __len__() – len() function
class Dataset:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

d = Dataset([1,2,3,4])
print(len(d))

# Example 8: Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.
class TwoDVector:
    def __init__(self, i , j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(1, 2, 3)
b.show()

# Example 9: Create a class ‘Employee’ and add salary and increment properties to it.
#Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
#which changes the value of increment based on the salary.

class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1)* 100

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.increment)

# Example 10: Write a class ‘Complex’ to represent complex numbers, along with overloaded
#operators ‘+’ and ‘*’ which adds and multiplies them.
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
        
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1*c2)

# Example 11: Write a class vector representing a vector of n dimensions. Overload the + and *
#operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  

print(v1 + v2)  
print(v1 * v2)  

print(v1 + v3)  
print(v1 * v3)  