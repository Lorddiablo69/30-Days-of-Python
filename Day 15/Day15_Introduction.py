# Types of errors

# Syntax error
# Most common type of error it occurs when the syntax are wrong.
# eg:
# print 'hello world'
# fix
print('hello world')

# Name error
# This type of error occurs when whe try to call a variable wehn we have not define it.
# eg:
# print(name)
# fix
name='sanyam'
print(name)

# Index error
# This type of error occurs when you work wiht indexes that are out of range or does not exists.
# eg:
# num=[1,2,3,4]
# print(num[4])
# fix
num=[1,2,3,4,5]
print(num[4])

# Module Not Found error
# This type of error occurs when you try to call the modules that does not exists or you mispelled the module name.
# eg:
# import maths
# fix
import math

# Attribute error
# This type of error occurs when you try to call the attrbutes that does not exist in the module or you mispelled it.
# eg:
# import math
# print(math.PI)
# fix
import math
print(math.pi)

# Key error
# This type of error occurs when there is the typo with the key or does not exist in the dictionaary.
# eg:
eg={'name':"Sanyam Shakya",'age':"24",'country':"Nepal"}
# print(eg['county'])
# fix
print(eg['country'])

# Type error
# This type of error occurs when you work wiht different data types, this usually occurs when you input the wrong datatype instead of similar data type.
# eg:
# print(2+'2')
# fix
print(2+2)

# Import error
# This type of error occurs when you try to import function form the module that doesnot exist or has a typo.
# eg:
# from math import power
# fix
from math import pow
print(pow(4,2))

# Value error
# This type of error occurs when you input a wrong value.
# eg:
# print(int('12a'))
# fix
print(int('12'))

# Zero Division error
# This type of error occurs when you work wiht 0 value that cannot be divided with.
# eg:
# print(2/0)
# fix
print(0/2) #we donot perform calculation like this and try to avoid the error but this is the demonstration only.