# Introduction to Data Types and built-in Functions in Python
# In Python we have lots of built-in functions. Some of the most commonly used Python built-in functions are the following:
#  print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir().
# Introduction to Variables

first_name = 'Sanyam'
last_name = 'Shakya'
age = 24
is_married = False

print("First Name:", first_name)
print(len(first_name))

# declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Sanyam', 'Shakya', 'Nepal', 24, False

print("Last Name:", last_name)
print("Age:", age)
print("Country:", country)
print("Married:", is_married)

# Getting user input

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

print("Your first name is:", first_name)
print("Your last name is:", last_name)  
print("Your age is:", age)

# Printing types of variables

print(type('Sanyam')) # str
print(type(24))      # int
print(type(9.8))    # float
print(type(True))   # bool
print(type([1, 2, 3])) # list
print(type((1, 2)))   # tuple
print(type({'name':'Sanyam', 'age':24})) # dict
print(type({9.8, 3.14, 2.7})) # set
print(type(1+2j))  # complex number
print(type(zip([1, 2, 3], ['a', 'b', 'c']))) # zip object

# Converting data types
# int to float
num_int = 10
num_float = float(num_int)
print("Integer:", num_int)
print("Converted to Float:", num_float)

# float to int
gravity = 9.81
gravity_int = int(gravity)
print("Float:", gravity)
print("Converted to Integer:", gravity_int)

# int to str
num = 100
num_str = str(num)
print("Integer:", num)
print("Converted to String:", num_str)

# str to int
num_str = "200"
num_int = int(num_str)
print("String:", num_str)
print("Converted to Integer:", num_int)

# str to list
first_name = "Sanyam"
first_name_list = list(first_name)
print("String:", first_name)
print("Converted to List:", first_name_list)    

