# # Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.

age=int(input('Enter your age:'))

if age>=18:
    print('You are old enough to Drive.')
else:
    years=18-age
    print(f'You need {years} years to drive.') 

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

my_age=24
your_age=int(input('Enter your age:'))

if my_age>your_age:
    diff=my_age-your_age
    if(diff==1):
        print('I am 1 year older than you.')
    else:
        print(f'I am {diff} years older than you.')
elif your_age>my_age:
    diff=your_age-my_age
    if(diff==1):
        print('You are 1 year older than me.')
    else:
        print(f'You are {diff} years older than me.')
else:
    print('We are the same age.')


# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.


a=int(input('Enter your a number a:'))
b=int(input('Enter your a number b:'))

if a>b:
        print('a is greater than b.')

elif b>a:
        print('b is greater than a.')
else:
    print('a is equal to b.')

# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

marks=float(input('Enter your scores:'))

if 100>=marks>=80:
     print('Your grade is A.')
elif 79>=marks>=70:
     print('Your grade is B.')
elif 69>=marks>=60:
     print('Your grade is C.')
elif 59>=marks>=50:
     print('Your grade is D.')
else:
     print('Your grade is F.')

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month=str(input('Enter the Month:'))

if month=='September'or month=='October'or month=='November':
     print('Season is Autumn.')
elif month=='December'or month=='January'or month=='February':
     print('Season is Winter.')
elif month=='March'or month=='April'or month=='May':
     print('Season is Spring.')
elif month=='June'or month=='July'or month=='August':
     print('Season is Summer.')
else:
     print('Enter correct month.')

# The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
inp=str(input('Enter a fruit:'))

if inp not in fruits:
     fruits.append(inp)
     print(f'Fruit added to the list the modified list:{fruits}')
else:
     print('That fruit already exist in the list.') 

# Here we have a person dictionary. Feel free to modify it!
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') -
#  for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills'in person:
    skills=person['skills']
    if len(skills)%2==1:
          middle=skills[len(skills)//2]
          print('Middle skill:',middle)
    elif 'pyhton'in person['skills']:
     print("Python skill found.")
    else:
        print('Python skill not found.')
else:
     print("Skills not found.")

if 'skills'in person:
    if 'JavaScript' and 'React'in person['skills']:
        print('He is a frontend developer.')
    elif'Node' and 'MongoDB' and 'Python' in person['skills']:
        print('He is a backend devloper.')
    elif'React'and'Node'and'MongoDB'in person['skills']:
         print('He is a fullstack developer.')
    else:
         print('Unknown Titile')
else:
     print("Skills not found.")

if person['is_marred']== True and person['country']=='Finland':
     print(f'{person["first_name"]} {person["last_name"]} is married and lives in {person["country"]}')
else:
     print('Required Condition not met.')
