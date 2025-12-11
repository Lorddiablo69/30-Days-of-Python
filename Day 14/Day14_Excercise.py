from countries_data import countries_data

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explain the difference between map, filter, and reduce.

# ->  map(function,iterable) it takes the individual value of the iterable and applies the function using each individual values and returns a new list
#     filter(function,iterable) it returns the only true boolean values of the condition used and provides a new list
#     reduce(function,iterable) it returns the single value of the iterable after function is completed

# Explain the difference between higher order function, closure and decorator

    # high order function is a function that takes order functions as a argument and returns  a function
    # clouser is where you taake the parameters from the outer function
    # decortor is where  function is wrap around another function with extra fucntionality

# Define a call function before map, filter or reduce, see examples.

def square(x):
    return x**2

def is_even(x):
    return x % 2 == 0

from functools import reduce
def add(x, y):
    return x + y
# You can pass these function to map, filter, reduce.

# Use for loop to print each country in the countries list.

for x in countries:
    print(x)

# Use for to print each name in the names list.

for x in names:
    print(x)

# Use for to print each number in the numbers list.

for x in numbers:
    print(x)

# Use map to create a new list by changing each country to uppercase in the countries 

def upper(count):
    return count.upper()

prnt=list(map(upper,countries))
print(prnt)

# Use map to create a new list by changing each number to its square in the numbers list

def sqr(count):
    return count**2

prnt=list(map(sqr,numbers))
print(prnt)

# Use map to change each name to uppercase in the names list

def upper(count):
    return count.upper()

prnt=list(map(upper,names))
print(prnt)

# Use filter to filter out countries containing 'land'.

land_countries=list(filter(lambda x: 'land' in x,countries))
print(land_countries)

# Use filter to filter out countries having exactly six characters.

chr_countries=list(filter(lambda x:len(x)==6 ,countries))
print(chr_countries)

# Use filter to filter out countries containing six letters and more in the country list.

chr_countries=list(filter(lambda x:len(x)>=6 ,countries))
print(chr_countries)

# Use filter to filter out countries starting with an 'E'

chr_countries=list(filter(lambda x:'E' in x,countries))
print(chr_countries)

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

from functools import reduce
sum_of_even_squares= reduce(lambda a,b:a+b,filter(lambda x:x%2==0,map(lambda x:x**2,numbers)))
print(sum_of_even_squares)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string

def get_string_lists(lst):
    return [x for x in lst if isinstance(x,str)]
print(get_string_lists(countries))

# Use reduce to sum all the numbers in the numbers list.

sumall=reduce(lambda a,b:a+b,numbers)
print(sumall)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

concatenate= reduce(lambda a,b: a +','+ b, countries[:-1])+' and'+' '+countries[-1]+' are north European countries' #countries[start:-1 which is second last element]
print(concatenate)

# Declare a function called categorize_countries that returns a list of countries with some common pattern 
# (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

from countries import countries

def categorize_countries(countries_list,pattern):
    p=pattern.lower()
    return [c for c in countries_list if p in c.lower()]

print(categorize_countries(countries,'land'))
print(categorize_countries(countries,'island'))
print(categorize_countries(countries,'ia'))
print(categorize_countries(countries,'stan'))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country 
# names starting with that letter.

def first_Letter_no(countries_list):
    result = {}  # declaring empty dictionary
    
    for country in countries_list:  # loop through each country in the list
        first = country[0]  # get the first letter of the country
        
        result[first] = result.get(first, 0) + 1  
        # If the letter doesn't exist, result.get(first,0) gives 0
        # Then we add 1 to increase count
    
    return result  # return the dictionary with letter counts

print(first_Letter_no(countries))

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js 
# list in the data folder.

def get_first_ten_countries(countries_list):
    return countries_list[:10]

print(get_first_ten_countries(countries))

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

def get_last_ten_countries(countries_list):
    return countries_list[-10:]

print(get_last_ten_countries(countries))

# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) 
# file and follow the tasks below:


# Sort countries by name, by capital, by population

sort_name=sorted(countries_data,key=lambda x:x['name'])
print(sort_name)
sort_capital=sorted(countries_data,key=lambda x:x['capital'])
print(sort_capital)
sort_population=sorted(countries_data,key=lambda x:x['population'])
print(sort_population)


# Sort out the ten most spoken languages by location.

from collections import Counter
lang_counter=Counter()
for country in countries_data:
    for lang in country.get('languages',[]):
        lang_counter[lang]+=1

top=lang_counter.most_common(10)
for lang,count in top:
    print(f'{lang},{count}')

# Sort out the ten most populated countries.

def most_populated(countries_data,n=10):
    sort_population=sorted(countries_data,key=lambda c:c.get('population',0),reverse=True)
    return [(c['name'], c.get('population',0)) for c in sort_population[:n]]
print(most_populated(countries_data,10))