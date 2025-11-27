# Assigning Different types of Variables
first_name = 'sanyam'
last_name= 'shakya'
full_name= 'Sanyam Shakya'
country= 'Nepal'
city= 'KTM'
age= 24
year= 2025
is_married= False
is_true= True
is_light_on= True

# Multiple Vriables
name,age,color,is_married= 'Sanyam Shakya',24,'red',False

# Checking Data Types
print(type(first_name))   # str
print(type(last_name))    # str
print(type(full_name))    # str
print(type(country))      # str
print(type(city))         # str
print(type(age))          # int
print(type(is_married))   # bool
print(type(is_true))      # bool
print(type(is_light_on))  # bool

print(len(first_name))   # length of first_name
print(len(last_name))    # length of last_name

num_one=5
num_two=4

total= num_one + num_two
diff= num_one - num_two
product= num_one * num_two
division= num_one / num_two
remainder= num_one % num_two

# num_one to the power of num_two
exp= num_one ** num_two

# Floor division of num_one by num_two
floor_div= num_one // num_two

print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_div)

radius= 30

area_of_circle= 3.14 * radius**2
circum_of_circle= 2 * 3.14 * radius
print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)

radius= int(input("Enter radius: "))
area_of_circle= 3.14 * radius**2
circum_of_circle= 2 * 3.14 * radius
print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)

first_name,last_name,country,age= input('enter your first name:'),input('enter your last name:'),input('enter your country:'),input('enter your age:')

help('keywords')
80