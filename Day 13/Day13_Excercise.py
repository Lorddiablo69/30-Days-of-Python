# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative=[i for i in numbers if i==0 or i<0]
print(negative)

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat=[num for row in list_of_lists for num in row]
flat2=[num for row in flat for num in row]
print(flat2)

# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

tuple_list=[(i,1,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(tuple_list)

# Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat=[[country.upper(),country[:3].upper(),capital.upper()] for [(country,capital)] in countries]
print(flat)

# Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lst=[{'country':country.upper(),'city':city.upper()} for [(country,city)] in countries]
print(lst)

# Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
joiname=[f'{first} {last}' for [(first,last)] in names]
print(joiname)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
m=lambda x1,y1,x2,y2:(y2-y1)/(x2-x1)
c=lambda m,x,y:y-m*x
print(m(1,2,2,1),c(2,2,7))