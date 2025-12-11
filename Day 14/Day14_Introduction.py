# Higher order function
# using functions as a parameters

def sum_numbers(num):        #normal function 
    return sum(num)

def high_order(f,lst):
    summation=f(lst)
    return summation

result=high_order(sum_numbers,[1,2,3,4,5])
print(result)

# Function as return value

def square(x):
    return x**2
def cube(x):
    return x**3
def absolute(x):
    if x>=0:
        return x
    else:
        return -(x)


def high_order(type):
    if type=='square':
        return square
    elif type=='cube':
        return cube
    elif type=='absolute':
        return absolute

result= high_order('square')
print(result(3))
result= high_order('cube')
print(result(3))
result= high_order('absolute')
print(result(-3))

# python closures
# nesting a function

def add_ten():
    ten = 10
    def add(num):
        return num+ ten
    return add

closure_result= add_ten()
print(closure_result(5))
print(closure_result(10))

# python decorators
# a decorator is a design pattern in python we caan dd new functionality to an existing object without
# modifyting its structure.

def uppercase_dec(function):
    def wrap():
        func=function()
        uppper=func.upper()
        return uppper
    return wrap
@uppercase_dec
def greeting():
    return 'welcome to python!!!!'

# OR
# def greeting():
#     return 'Welcome to Python'
# greeting = uppercase_dec(greeting)

print (greeting())

# applyng multiple decorators to a single function

def uppercase_dec(function):
    def wrap():
        func=function()
        uppper=func.upper()
        return uppper
    return wrap

def split_dec(function):
    def wrap():
        func=function()
        split=func.split()
        return split
    return wrap

# @uppercase_dec
# @split_dec
# def greeting():
#     return 'welcome to pyhton using two decorators'   #order is important as it varies according to order whle calling bottom one gets called first
# print(greeting())


@split_dec
@uppercase_dec
def greeting():
    return 'welcome to pyhton using two decorators'
print(greeting())

# accepting paramets in decorator functions

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("sanyam", "shakya",'nepal')

# high order function
# map function

numbers=[1,2,3,4,5]
sq=map(lambda x:x**2 ,numbers)
print(list(sq))

numbers_str = ['1', '2', '3', '4', '5']  # iterable
print(list(numbers_str))
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

a = [1,2,3]
b = [10,20,30]
sum_pairs = list(map(lambda x, y: x + y, a, reversed(b)))
print(sum_pairs)  # [11, 22, 33]

# filter function
# basically when calls it takes the satisfactory critera in boolean form(true)

def pt(num):
    if num == 1 or num==5:
        return True
    return False

ptt=filter(pt,numbers)
print(list(ptt))

# reduce function
# it is use to gian a single value from list 

from functools import reduce
numbers=['1','2','3','4','5','6','7','8','9','10']
numbers=list(map(int,numbers))

def add_even_numbers(x,y):
    if y%2==0:
        return x+y
    else:
        return x
even=reduce(add_even_numbers,numbers,0) #start from 0
print(even)