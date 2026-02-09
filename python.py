
#! Naming Conventions

# MyName = "haris" #pascal case

# myName = "haris" #camel case

# my_name = "haris" #snake case

#! Data Type

#? Integer

# a = 70
# b = 30
# c = 100

# print(type(a))
# print(a + b + c)

#? Float

# a = 1.2

# print(type(a))

#? Complex

# a = 100j

# print(type(a))

#? Strings

# str = "haris"

# print(type(str))

#? Boolean

# boolTrue = True
# boolFalse = False

# print(type(boolTrue))
# print(type(boolFalse))

#! Strings and type conversion 

#? How Strings work

#* Unicode

# a = "#"

# print(ord(a))

# b = 35

# print(chr(b))

# c = "😊"

# print(ord(c))

# d = 128522

# print(chr(d))

#? String Indexing 
        
# a = "hello world"

# print(a[-7])
# print(a[4])

#? String Slicing

# a = "hello world"

# print(a[6:11:1])
# print(a[6::1])

#? Type conversion  
#* int()
#* float()
#* str()
#* bool()

#? int()

# a = "10"
# a = int(a)

# print(type(a))

#? float()

# a = 12
# a = float(a)

# print(type(a))

#? str()

# a = 12
# a = str(a)

# print(type(a))

#? bool()

# a = 0
# b = 1

# print(bool(a))
# print(bool(b))

#! important 

#? falsy values
#* false
#* 0
#* 0.0
#* " "
#* []
#* ()
#* {}

#? truthy values
#* All values that are not falsy are considered truthy


#? Type conversion types
#* There are 2 types of conversion "Implicit" and "Explicit"

#? Explicit
#* In this we as a user use in build functions to convert one data type to another

#* example

#* int()
#* float()
#* str()
#* bool()

#? Implicit
#* In this python automatically converts data from one data type to another.

#* example 

# a = 12

# print(a/3)

#! Input and output

#? Input
#* But the main question is how to ask user for some information.

#* exmaple

# name = input("what is your name")
# age = input("what is your age")

# print(f"hello, my name is {name} and i am {age} year old")

#! important 

#* f mean formatted string



#? Output 
#* You probably know till now, how to provide the output of the code you have written and that is with print() function.

#* example

# name = "haris"
# age = 15

# print( name , age ) # it is called output

#! Operators
#* Operators are symbols that perform operations on variables and values.

#? Arithmetic operators 
#* addition  +
#* subtraction -
#* multiplication *
#* division /
#* Floor division // 
#* modulus %
#* Exponentiation **

#? addition +

# a = 10
# b = 10

# print(a + b)

#? subtraction -

# a = 15
# b = 10

# print(a - b)

#? multiplication *

# a = 5
# b = 10

# print(a * b)

#? division /

# a = 50
# b = 5

# print(a / b)

#? Floor division //

# a = 50
# b = 5

# print(a // b)

#? modulus %

# a = 32
# b = 6

# print(a % b)

#? Exponentiation **

# a = 7**2

# print(a)

#! important 
#* phython follow BODMAS rule
#* BODMAS ( [B] brackets , [O] orders , [DM] Division , [AS] Addition )

#* example 

# print(12 + 4 // 2)

#? Assignment operator
#* Assignment operators are used to assign values to variables.
#* Python also provides compound assignment operators that
#* perform operations like addition, subtraction, multiplication, etc

#! important
#* A basic assignment operator is simple = 

#? Compound assignment operator
#* += Add and assign
#* -= Subtract and assign
#* *= Multiply and assign
#* /= Divide and assign
#* //= Floor divide and assign
#* %= modulus and assign
# * **= Exponentiation and assign

#? += Add and assign

# a = 20
# a += 20 + 40 + 60

# print(a)

#? -= Subtract and assign

# a = 140
# a -= 40

# print(a)

#? *= Multiply and assign

# a = 20
# a *= 20

# print(a)

#? /= Divide and assign

# a = 20
# a /= 5

# print(a)

#? //= Floor divide and assign

# a = 20
# a //= 5

# print(a)

#? %= modulus and assign

# a = 20
# a %= 5

# print(a)

#? **= Exponentiation and assign

# a = 20
# a **= 5

# print(a)

#? Comparison operator
#* == Equal to
#* != Not Equal to
#* > Greater than
#* < Less than
#* >= Greater than or equal to
#* <= Less than or equal to

#? == Equal to

# print(5 == 5)

#? != Not Equal to

# print(5 != 5)

#? > Greater than

# print(6 > 5)

#? < Less than

# print(6 < 5)

#? >= Greater than or equal to

# print(6 >= 5)

#? <= Less than or equal to

# print(6 <= 5)

#! important 
#* Strings will be comparing the Ascii values of string

#* example

# print(ord("A"))
# print(ord("a"))

# print("A" < "a")

#? Logical operators 
#* and - Return True if both condition are True.
#* or - Return True if at least one condition is True.
#* not - Reverse the boolean value.

#? and 

# print(150 > 100 and 50 == 50)
# print(50 > 100 and 50 == 50)

#? or

# print(100 > 100 or 51 == 50)
# print(100 > 100 or 50 == 50)

#? not

# print(not 100 == 100)
# print(not 150 == 100)

#? Trivial Questions 

# print(126 > 130) #* false
# print((456 == 456) != (235 == 236)) #* true
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13) #* true
# print(True and bool(0)) #* false

#! Conditional statements
#* Conditional statements in Python allow decision-making by
#* executing different blocks of code based on conditions.

#? Types of conditional statements
#* if - Executes if the condition is True
#* if-else - Executes if True, another if False
#* if-elif-else - Checks multiple condition in sequence.

#? if

# a = 100

# if a > 50:
#     print(True)

#? if-else

# a = 15

# if a <= 16 and 35 != 35:
#     print("true")
# else:
#     print("false")    

#? if-elif-else

# money = int( input( "please provide me the money" ) )

# if money == 50:
#     print("i eat french fries")
# elif money == 100:
#     print("i eat burger")
# elif money == 150:
#     print("i eat pizza")
# elif money < 100:
#     print("i eat chips , biscuits")         
# else:
#     print("cry")
        
#? Some Questions on Conditional 

#* Q1

# num1 = input("enter a first number ")
# num2 = input("enter a second number ")

# if(num1 > num2):
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num2} is greater than {num1}")    
# else:
#     print("both number are similar")    

#* Q2

# gender = input("what your gender , male or female ")

# if gender == "male":
#     print(f"your gender is {gender}")
# elif gender == "female":
#     print(f"hello {gender}")
# else:
#     print("enter a valid gender")    

#* Q3

# num = int(input("enter a number :- "))

# if num%2 == 0:
#     print("your number is even")
# else:
#     print("your number is odd")    

#* Q4

# name = input("enter your name ")
# age = int(input("enter your age "))

# if age >= 18:
#     print(f"hello {name}, you are eligible for vote")
# else:
#     print(f"hello {name}, you are not eligible for vote")

#* Q5

# year = int(input("enter a year "))

# if year %100 == 0 and year %400 == 0:
#     print(f"its a leap {year}")
# elif year %100 != 0 and year %4 == 0:
#     print(f"its a leap {year}")
# else:
#     print(f"its not a leap {year}")

#? if elif ladder

# temperature = int(input("enter the temperature "))

# if temperature < 0:
#     print("freezing cold")
# elif temperature >= 0 and temperature <= 10:
#     print("very cold")
# elif temperature >= 10 and temperature <= 20:
#     print("cold")
# elif temperature >= 20 and temperature <= 30:
#     print("pleasent")
# elif temperature >= 30 and temperature <= 40:
#     print("hot")
# else:
#     print("very hot")    

#! Loops

#? Loops in python 














