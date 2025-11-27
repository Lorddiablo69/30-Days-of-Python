word_1='Thirty'
word_2='Days'
word_3='Of'
word_4='Python'
word_5='Coding'
word_6='For'
word_7='All'

formatted_string_1=f'{word_1} {word_2} {word_3} {word_4}'
formatted_string_2=f'{word_5} {word_6} {word_7}'

print(formatted_string_1)
print(formatted_string_2)

company='Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.find('Coding'))
print(company.rfind('Coding'))
print(company.index('Coding'))
print(company.rindex('Coding'))
print(company.replace('Coding','Python'))
print('Python for everyone'.replace('everyone','all'))
print(company.split(' '))
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', '))
print(company[0])
print(company[-1])
print(company[10])

# to find the acronym of "Python For Everyone"

word='Python For Everyone'
Capitalized_Words=word.title()
Acronym=''.join([letter[0] for letter in Capitalized_Words.split(' ')])
print(Acronym)

# to find the acronym of "Coding For All"

word='Coding for all'
Capitalized_word=word.title()
Acronym=''.join(word[0] for word in Capitalized_word.split(' '))
print(Acronym)

print(word.index('C'))
print(word.index('F'))
print('Coding for all People'.rindex('l'))
print('You cannot end a sentece with because because because is a conjunction'.index('because'))
print('You cannot end a sentece with because because because is a conjunction'.rindex('because'))
print('You cannot end a sentece with because because because is a conjunction'.split('because because because'))
print('  Coding For All  '.strip())
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

list_of_python_libaries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list_of_python_libaries))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

radius=10
area=3.14 * radius**2
print(f'The area of a circle with radious{radius}is{area}meters square.')

a=8
b=6

print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}%{b}={a%b}')
print(f'{a}//{b}={a//b}')
print(f'{a}**{b}={a**b}')
