# Introdduction to Assignment Operators in Python
# Assignment operators are used to assign values to variables.
# The basic assignment operator is the equal sign (=).

x=5 #x is assigned the value of 5
x += 3 #x is increased by 3 (x = x + 3)
x-=3 #x is decreased by 3 (x = x - 3)
x *= 3 #x is multiplied by 3 (x = x * 3)
x /= 3 #x is divided by 3 (x = x / 3)
x %= 3 #x is assigned the remainder of x divided by 3 (x = x % 3)
x **= 3 #x is raised to the power of 3 (x = x ** 3)
x //= 3 #x is assigned the floor division of x by 3 (x = x // 3)
x&=3 #x is assigned the bitwise AND of x and 3 (x = x & 3)
x|=3 #x is assigned the bitwise OR of x and 3 (x = x | 3)
x^=3 #x is assigned the bitwise XOR of x and 3 (x = x ^ 3)
x>>=3 #x is assigned the bitwise right shift of x by 3 (x = x >> 3)
x<<=3 #x is assigned the bitwise left shift of x by 3 (x = x << 3)

# arithmentic operators combined with assignment operators

a=3
b=2

# Arithmetic operations with assignment
total= a + b
diff= a - b
product= a * b
division= a / b
remainder= a % b
exp= a ** b
floor_div= a // b

print('a+b=', total)
print('a-b=', diff)
print('a*b=', product)
print('a/b=', division)
print('a%b=', remainder)
print('a**b=', exp)
print('a//b=', floor_div)

# Calculating area of a circle

raadius =10
area_circle = 3.14 * raadius**2 #two* sign means power
print('Area of circle with radius', raadius, 'is:', area_circle)

# Calculating area of a rectangle

length = 10
width =20
area_rectangle = length * width
print('Area of rectangle with length', length, 'and width', width, 'is:', area_rectangle)

# Calculating a weight of an object
mass = 75 # in kg
gravity = 9.81 # in m/s^2
weight = mass * gravity
print('Weight of the object is:', weight, 'N')

# Calculating the density of a Liquid
mass=75 # in kg
volume=0.075 # in m^3
density= mass / volume
print('Density of the liquid is:', density, 'kg/m^3')

# Comparison Operators

print(3 > 2)  # True, because 3 is greater than 2
print(3 < 2)  # False, because 3 is not less than 2
print(3 >= 2) # True, because 3 is greater than or equal to 2
print(3 <= 2) # False, because 3 is not less than or equal
print(3 == 2) # False, because 3 is not equal to 2
print(3 != 2) # True, because 3 is not equal to 2

print('A in Asabeneh', 'A' in 'Asabeneh') # True, because 'A' is found in 'Asabeneh'
print('B in Asabeneh', 'B' in 'Asabeneh') # False, because 'B' is not found in 'Asabeneh'
print('a in an:', 'a' in 'an') # True, because 'a' is found in 'an'
print('4 is 2*2:', 4 is 2*2) # True, because 4 is the same as 2*2
print('4 is not 2*3:', 4 is not 2*3) # True, because 4 is not the same as 2*3
print('4is 2**2:', 4 is 2**2) # True, because 4 is the same as 2**2

# Logical Operators
print(3 > 2 and 4 > 3) # True, because both expressions are true
print(3 > 2 and 4 < 3) # False, because one of the expressions is false
print(3 > 2 or 4 > 3)  # True, because both of the expressions is true
print(3 < 2 or 4 < 3)  # False, because both of the expressions is false

print(3>2 or 4>3) # True, because both of the expressions is true
print(3>2 or 4<3) # True, because one of the expressions is true
print(3<2 or 4<3) # False, because both of the expressions is false

print(not 3>2) # False, because 3>2 is true, not true is false
print(not True) # False, because not true is false
print(not False) # True, because not false is true

print(not not True) # True, because not false is true
print(not not False) # False, because not true is false 
