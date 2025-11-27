# Introduction to Strings in Python
# Multiline string
multiline_string = ''' this is a multiline string
thaat can spans multiple lines
and preserves the line breaks.  
It is useful for long text blocks.'''
print(multiline_string)

# String concatenation
first_name = "Sanyam"
last_name = "Shakya"
space=' '
full_name= first_name + space + last_name
print("Full Name:", full_name)

# escape sequences
# \n for new line, \t for tab, \\ for backslash
# \' for single quote, \" for double quote
print('This is an example of line break.\nThis is the next line.') # New line
print("\tdays\tTopics\tExercises")
print('day 1\t3\t5')
print('day 2\t4\t5')
print("day 3\t2\t5")
print('This is bckslash (\\)') # Backslash
print('This is how you write \'single quote\' and \"double quote\"')

# old style string formatting
# %s for string, %d for integer, %f for float , %.number of digitsf for floatng point number with fixed precision

first_name = "Sanyam"
last_name = "Shakya"
age = 20
hobies = ['anime','coding','gaming']
formatted_string='My name is %s %s. I am %d yeaars old. My hobies are: %s'%(first_name,last_name,age,hobies)
print(formatted_string)

# new style string formatting
first_name = "Sanyam"
last_name = "Shakya"
age = 20
hobies = ['anime','coding','gaming']
formatted_string='My name is {} {}. I am {} years old. My hobies are: {}.Ths is new string formatted'.format(first_name,last_name,age,hobies)
print(formatted_string)

a=2
b=3

print('{}+{}={}'.format(a,b,a+b))
print('{}-{}={}'.format(a,b,a-b))
print('{}*{}={}'.format(a,b,a*b))
print('{}/{}={}'.format(a,b,a/b))
print('{}%{}={}'.format(a,b,a%b))
print('{}//{}={}'.format(a,b,a//b))
print('{}**{}={}'.format(a,b,a**b))

# string interpolation (f-strings)
a=2
b=3
print('This is f-string formatted')
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}%{b}={a%b}')
print(f'{a}//{b}={a//b}')
print(f'{a}**{b}={a**b}')

language='Python'
first_letter=language[0]
print(f'first letter ={first_letter}')
second_letter=language[-5]
print(f'second letter ={second_letter}')
last_index=len(language) -1
last_letter= language[last_index]
print(f'last letter ={last_letter}')

# string slicing
language='Python'
first_three=language[0:3]
print(f'first three letters ={first_three}')
last_three=language[-3:]
print(f'last three letters ={last_three}')

# reversing a string
language='Python'
reverse=language[::-1]
print(f'reversed string ={reverse}')

# skipping characters
language='Python'
skip=language[0:6:2]
print(f'skipping characters ={skip}')

# string methods
# capitalize() converts the first character to uppercase
# count() returns the number of occurrences of a substring in the string
# endswith() checks if the string ends with a specified 
# expandtabs() replaces tab characters with spaces
# find() returns the lowest index of the substring if found
# rfind() returns the highest index of the substring if found
# format() formats specified values in a string
# index() returns the lowest index of the substring
# rindex() returns the highest index of the substring
# isalnum() checks if all characters are alphanumeric
# isalpha() checks if all characters are alphabetic
# isdecimal() checks if all characters are decimal characters
# isdigit() checks if all characters are digits
# isnumeric() checks if all characters are numeric
# isidentifier() checks if the string is a valid identifier
# islower() checks if all characters are lowercase
# isupper() checks if all characters are uppercase
# join() joins the elements of an iterable to the end of the string
# strip() removes any leading and trailing characters (space is the default)
# replace() replaces a substring with another substring
# split() splits the string at the specified separator and returns a list
# title() converts the first character of each word to uppercase
# swapcase() converts uppercase characters to lowercase and vice versa
# startswith() checks if the string starts with a specified substring


strings='thirty days of python'
print(strings.capitalize())
print(strings.count('y')) #counts number of y in the string
print(strings.count("y",7,18)) #counts number of y between index 7 and 14

print(strings.endswith('on')) #if ends with on it gives true
print(strings.endswith('tion')) #if ends with tion it gives false

print('hello\tworld\t!'.expandtabs())
print('hello\tworld\t!'.expandtabs(5)) #5 spaces for each tab

print(strings.find('y')) #first occurence of y
print(strings.rfind('y')) #last occurence of y

print('My name is {} {}'.format('Sanyam','Shakya'))

print(strings.index('y')) #first occurence of y
print(strings.rindex('y')) #last occurence of y
print(strings.index('z')) #gives error as z is not in the string
print(strings.rindex('z')) #gives error as z is not in the string

print('Python3'.isalnum()) #all are alphanumeric
print('Pyhton@@'.isalnum()) #not all are alphanumeric

print('Python'.isalpha()) #all are alphabetic
print('234'.isalpha()) #not all are alphabetic

print('234'.isdecimal()) #all are decimal characters
print('23.4'.isdecimal()) #not all are decimal characters

print('234//BAu'.isdigit()) #all are digits
print('python'.isdigit()) #not all are digits

print('234//34'.isnumeric()) #all are numeric
print('23.4/@'.isnumeric()) #not all are numeric

print('thirty_days of python2'.isidentifier()) #valid identifier
print(strings.isidentifier()) #not a valid identifier

print('python'.islower()) #all are lowercase
print('Python'.islower()) #not all are lowercase

print('PYTHON'.isupper()) #all are uppercase
print('PYThon'.isupper()) #not all are uppercase

web_tech=['HTML','CSS','JS','React']
print(' '.join(web_tech)) #joins with space
print('##'.join(web_tech)) #joins with ##

print(strings.strip('th')) #removes leading and trailing th

print(strings.replace('thirty','30')) #replaces 'thirty' with '30'

print(strings.split()) #splits at space
strings='thirty days of##python'
print(strings.split('##')) #splits at ##

print('hello world'.title()) #first letter of each word is capitalized

print('HeLLo WoRLD'.swapcase()) #uppercase to lowercase and vice versa

print(strings.startswith('thirty')) #if starts with thirty it gives true
print(strings.startswith('30')) #if starts with 30 it gives false





