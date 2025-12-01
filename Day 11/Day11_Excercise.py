from countries_data import countries_data
import math
import cmath

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def sum(a,b):
    sum_of_two_numbers=a+b
    return sum_of_two_numbers
print(sum(2,5))
    
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(r):
    area=3.14*r**2
    return area
print(f'The area of circle is {area_of_circle(2)}')

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*num):
    if not num:
        return 0
    total=0
    for item in num:
        if not isinstance(item,(int,float)):
            raise TypeError('All data type should be integers or float')
        total+=item
    return total
print(add_all_nums(2,2,4))
print(add_all_nums(2,2,3,4,4))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F,
#  convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    fahren=(celsius*(9/5))+32
    return fahren
print(convert_celsius_to_fahrenheit(233))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month in ("september", "october", "november"):
        return "Autumn"
    if month in ("december", "january", "february"):
        return "Winter"
    if month in ("march", "april", "may"):
        return "Spring"
    if month in ("june", "july", "august"):
        return "Summer"
print(check_season('january'))

# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1,y1,x2,y2):
    return(y2-y1)/(x2-x1)
print(calculate_slope(1,2,4,5))

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, 
# solve_quadratic_eqn.

def quadratic(a,b,c):
    if a==0:
        if b==0:
            raise ValueError('not an eution')
        return(-c/b,)
    d=b**2-4*a*c
    if d>=0:
        x1=(-b+ math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
    else:
        x1=(-b+ cmath.sqrt(d))/(2*a)
        x2=(-b-cmath.sqrt(d))/(2*a)
    return(x1,x2)
print(f'The solution of given equation are x={quadratic(2,4,8)}')

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(*lst):
    for item in lst:
        print(item)
print(print_list(2,3,4,5,6,8,7,9))

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(lst):
    rev=[]
    for i in range(len(lst)-1,-1,-1):
        rev.append(lst[i])
    return rev
print(reverse_list([1,2,3,4,5]))
print(reverse_list(['a','b','c']))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst):
    cap=[]
    for i in lst:
        cap.append(i.capitalize())
    return cap
print(capitalize_list_items(['sanyam','shakya']))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(lst,item):
    lst.append(item)
    return lst
print(add_item([1,2,3,4],5))
print(add_item(['math','science'],'computer'))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(lst,item):
    lst.remove(item)
    return lst
print(remove_item([1,2,3,4,5],5))
print(remove_item(['math','computer','science'],'computer'))

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050

def sum_of_numbers(n):
    total=0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_odds(n):
    total=0
    for i in range(n+1):
        if i%2!=0:
            total+=i
    return total
print(sum_of_odds(5))

def sum_of_even(n):
    total=0
    for i in range(n+1):
        if i%2==0:
            total+=i
    return total
print(sum_of_even(5))

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.

def evens_and_odds(n):
    n=abs(n)
    count_evens=0
    count_odds=0
    for i in range(n+1):
        if i%2==0:
            count_evens+=1
        else:
            count_odds+=1
    return(count_odds,count_evens)
odd,even=evens_and_odds(100)
print(f'The number of odds are {odd}\nThe number of evens are {even}')

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return fact
print(factorial(5))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(n):
    if n is None:
        return("It is empty")
    else:
        return('It is not empty')
print(is_empty(None))

# Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import statistics

def calculate_mean(data):
    if not data:
        return None
    return statistics.mean(data)

def calculate_median(data):
    if not data:
        return None
    return statistics.median(data)

def calculate_mode(data):
    if not data:
        return None
    try:
        return statistics.mode(data)
    except statistics.StatisticsError:
        # multiple modes or no unique mode -> provide frequencies or list of modes
        freq = Counter(data)
        max_count = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_count]
        return modes

def calculate_range(data):
    if not data:
        return None
    return max(data) - min(data)

def calculate_variance(data):
    if not data:
        return None
    if len(data) == 1:
        return 0.0
    return statistics.pvariance(data)  # population variance

def calculate_std(data):
    if not data:
        return None
    if len(data) == 1:
        return 0.0
    return statistics.pstdev(data)  # population std dev
print(calculate_mean([1,2,3,4,5]))
print(calculate_median([1,2,3,4,5]))
print(calculate_mode([1,2,3,4,5]))
print(calculate_range([1,2,3,4,5]))
print(calculate_variance([1,2,3,4,5]))
print(calculate_std([1,2,3,4,5]))

# Write a function called is_prime, which checks if a number is prime.

def is_prime(n):
    if n%2==0 and n<=1:
        return False
    r=int(math.sqrt(n))
    for i in range(3,r,2):
        if n%i==0:
            return False
    return True
print(is_prime(83))

# Write a functions which checks if all items are unique in the list.

def unique(lst):
    return len(lst)==len(set(lst))

print(unique(['animal','pet','chicken']))
print(unique(['animal','pet','chicken','animal']))

# Write a function which checks if all the items of the list are of the same data type.

def same_data(lst):
    if not lst:
        return True
    typ=type(lst[0])
    return all(type(x) is typ for x in lst)

print(same_data([1,2,3,4,5]))
print(same_data([1,'w',3,4,5]))

# Write a function which check if provided variable is a valid python variable

import keyword
def is_valid_variable(name):
    if not isinstance(name,str):
        return False
    return name.isidentifier() and not keyword.iskeyword(name)
print(is_valid_variable('a'))
print(is_valid_variable('for'))

# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

from collections import Counter

def most_spoken_languages(countries_data,top=10):
    lang_count=Counter()
    for country in countries_data:
        langs=country.get("languages",[])
        for l in langs:
            lang_count[l] += 1
    return lang_count.most_common(top)
print(most_spoken_languages(countries_data,top=10))

def most_populated_countries(countries_data,top=10):
        population=[c for c in countries_data if 'population' in c and 'name' in c]
        sort=sorted(population,key=lambda x:x['population'],reverse=True)
        return [(c['name'],c['population']) for c in sort[:top]]
print(most_populated_countries(countries_data,top=10))
    
