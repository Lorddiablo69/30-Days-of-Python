# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Foodmandu','esewa','Khalti'])
it_companies.remove('Khalti')
print(it_companies)

# Joing A and B
print(A.union(B))
print(B.union(A))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))

# Deleting Set
del A
del B

set_age=set(age)
print(len(set_age))
print(len(age))

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.lower().replace(".", "").split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Total unique words:", len(unique_words))
