# Introduction
# while loop
count=0
while count<5:
    print(count)
    count=count+1
else:
    print(count)

# break statement
count=0
while count<5:
    print(count)
    count=count+1
    if count==3:
        break

# countinue statement
count=0
while count<5:
    if count==3:
        count=count+1
        continue
    print(count)
    count=count+1

# for loop
# for loop with list
numbers=[1,2,3,4,5,6]
for nr in numbers:
    print(nr)

# for loop with string
language='Python'
for let in language:
    print(let)

# above code is equivalent to
language='Python'
for i in range(len(language)):
    print(language[i])

# for loop with tuple
numbers=(1,2,3,4,5,6)
for nr in numbers:
    print(nr)

# for loop with dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

# for loop in set
comp={'facebook','google','tiktok','apple','IBM','Amazom'}
for c in comp:
    print(c)

# break in for Loop 
num=(1,2,3,4,5)
for n in num:
    print(n)
    if n==3:
        break

for n in num:
    print(n)
    if n==3:
        continue
    print('Next number is ',n+1) if n!=5 else print('loop end')
print('outside the loop')

# range function
# this is used in list number in list sets etc
# this function can take 3 arguments (start,end,increment) but it can still be run using one argumen that is end
print(f'The odd number upto 10 are: {list(range(1,10,2))}')
print(f'The even number upto 10 are: {set(range(0,11,2))}')

# nested for loop
# we can write loop inside a loop
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    if key=='skills':
        for skill in person['skills']:
            print(skill)
else:
    print('These are the all the skills')            

# Pass
# this statement is used to avoid errors or s  placeholder
for number in range(6):
    pass