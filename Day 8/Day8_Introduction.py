# Introduction
# Creating a dictionary
empty_dict={}

# Dictionary with data value
dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}

# Dictionart can have any type of data as value
person = {
    'first_name':'Sanyam',
    'last_name':'Shakya',
    'age':24,
    'country':'Nepal',
    'is_marred': False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
# Checking Dictionary length
print(len(person))

# Accessing Dictionary
print(person['first_name'])

# To Check is the key value exist or not and to get the access of data without raising and error
print(person.get('company'))
print(person.get('age'))

# Adding Items to a Dictionary
person['hobbies']= ['anime','movie','coding']
print(person)

# Modifyiing Dictionary
person['address']= {
        'street':'Teku,KTM',
        'zipcode':'12'
    }
print(person)

# Checking Dictionary
print('first_name' in person)

# Removing key and Value form a Dictionary
person.pop('age')
print(person)
person.popitem() #remove last item
print(person)
del person['address'] #remove 'address' item
print(person)

# Changing  Dictionary to list of tuples
print(person.items())

# Clearing Dictionary
person = {
    'first_name':'Sanyam',
    'last_name':'Shakya',
    'age':24,
    'country':'Nepal',
    'is_marred': False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(person.clear())

# Deleting Dictionary
del person

# Copying Dictionary
person = {
    'first_name':'Sanyam',
    'last_name':'Shakya',
    'age':24,
    'country':'Nepal',
    'is_marred': False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

person_cpy=person.copy()
print(person_cpy)

# To get tha all the keys of dictionary as a list
print(person.keys())

# Ro get all the values as a list of Dictionary
print(person.values())
