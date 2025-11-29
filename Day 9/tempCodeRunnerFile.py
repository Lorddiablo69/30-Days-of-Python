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
