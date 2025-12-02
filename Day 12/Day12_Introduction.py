# Intoroduction to modules
# it is a file containing a set of codes or functions which can be included to an application
# creating a module
# module created in mymodule.py now importing it
import mymodule
print(mymodule.generate_full_name('Sanyam','Shakya'))

# we can import multiple functions nand use it
# from mymodule import generate_full_name, other functions...
# renaming the imported module
from mymodule import generate_full_name as fullname
print(fullname('sanyam','shakya'))

# Import built-in modules
import os

# creating directory
# os.mkdir('test1')
# changing directory
# os.chdir('path')
# getting working directory currently
# os.getcwd()
# # removing directory
# os.rmdir()

# import sys
# #print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# # python script.py Asabeneh 30DaysOfPython

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive