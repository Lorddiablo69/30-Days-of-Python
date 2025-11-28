# Create an empty dictionary called 
dog={}

# Add name, color, breed, legs, age to the dog dictionary
dog={'Name':'Rocky','Color':'Brown','Breed':'Husky','Legs':4,'age':2}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={'first_name':'Sanyam','last_name':'Shakya','gender':'Male','age':24,'martial_status':False,'skills':['HTML','CSS','JS'],'country':'Nepal','city':'KTM','address':'Teku'}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(f'The value of skills are {student.get('skills')} and its data type is {type(student.get('skills'))}')

# Modify the skills values by adding one or two skills
student['skills'].append('Python')
student['skills'].append('React')
print(student['skills'])

# Get the dictionary keys as a list
print(student.keys())
lst=list(student.keys())
print(lst)

# Get the dictionary values as a list
print(student.values())
lst=list(student.values())
print(lst)

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
del student['address']
print(student)

# Delete one of the dictionaries
del student
