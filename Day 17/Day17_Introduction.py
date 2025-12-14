# exception handling
# It is a method where we ensure that the a program runs smoothly and if ever the error occurs regardless of any reason it will
# handle it gracefully and make sure that rest of the part of program runs smoothly.
# try and except

try:
    print(10 +'5')
except:
    print('something went wrong')

try:
    name=input('enter your name:')
    year_born=input('year born:')
    age=2019-year_born
    prnt(f'you are {name} and you are {age} year old')
except TypeError:
    print('Type error occured')
except ValueError:
    print('value error occured')
except ZeroDivisionError:
    print('zero division error occured')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2025 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

# packng and unpacking arguments
# * for tuples and ** for dictionaries
# unpacking

def sum(a,b,c,d,e):
    return(a+b+c+d+e)
lst=[1,2,3,4,5]
print(sum(lst)) #throws a error

def sum(a,b,c,d,e):
    return(a+b+c+d+e)
lst=[1,2,3,4,5]
print(sum(*lst)) #unpacks the list

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

# unpakcing dictonaries
def unpack(name,country,city,age):
    return f'{name} lives in {country},{city}.He is {age} year old.'
dct={'name':'Sanyam',
     'country':"Nepal",
     'city':'KTM',
     "age":24,
          
     }

print(unpack(**dct))

# Packing
def sum(*num):
    s=0
    for i in num:
        s+=i
    return s
print(sum(1,2,3,4,5))

# packing Dictonaries
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=2502))

# spreading in Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# enumerate
# if we need a index in a list we can use enumerate a built in function to get the index of each tem in the list
for index, item in enumerate([20,30,40]):
    print(index,item)

countries=['Finland','Nepal']
for position, item in enumerate(countries):
    if item == 'Nepal':
        print(f'The country {item} has been found at index {position}')
        
# Zip
fruits=['apple','banana','mango','orange','kiwi']
veg=['potato','onion','tomato','carrot']
combine=[]
for f,v in zip(fruits,veg):
    combine.append({'fruits':f,"veg":v})
print(combine)
