# Introduction to functions
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name ()) # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

# Passing function with parameters

def multiply_two_number (num1):
    num2=int(input('enter a number:'))
    product=num1*num2
    return product
print(multiply_two_number(10))

# Passing function with two or more parameters

def multiply_two_number (num1,num2):
    product=num1*num2
    return product
print(multiply_two_number(10,20))

def multiply_two_number (num1,num2):
    product=num1*num2
    return product
print(multiply_two_number(num1=10,num2=20))

# we can pass multiple values to a function if we are not sure
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
