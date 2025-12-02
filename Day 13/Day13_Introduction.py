# List Comprehension
# [i for i in iterable if expression] syntax
# Change a string to a list of characters
# first method
language='python'
lst = list(language)
print(type(lst))
print(lst)

# second method
lst=[i for i in language]  #list comprehension
print(type(lst))
print(lst)

# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# list comprehension can be combined with if expression

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# lambda function
# creating aa lambda function
# to create lambda function we lambda as a keyword followed by a parameters followed by a expression
# example of adding two numbers using lambda function
sum_two_num= lambda a,b: a+b
print(sum_two_num(2,8))

# or another method
print((lambda a,b:a+b)(2,3))

# printing square
print((lambda a:a**2)(2))

# printing cube
print((lambda a:a**3)(2))

# example of multiple variables
var=lambda a,b,c: a**2 - 3 * b + 4 * c 
print((var(5,5,3)))

# lambda function in another function
# function to find the exponential oof given numbers

def expo(x):
    return lambda n:x**n
power=expo(5)(3)
print(power)
