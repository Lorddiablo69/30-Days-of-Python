# set
# Creating set
st=set() #empty set
st={1,2,3,4,5}

# Acessing item in set
st={'sanyam','shakya',24,'Nepal'}
print('sanyam'in st)
st.add('Male')
print(st)
st.update([1,2,3,4,5])
print(st)
st.remove(2)
print(st)
st.pop() #remooves random item from the list
st.clear() #empty set
del st #deletes the set

# Converting list to sets
lst=[1,2,33,4,5]
print(lst)
st=set(lst)
print(st)

# joining sets
st1={1,2,3}
st2={4,5,6}
st3=st1.union(st2)
print(st3)

# updating items of sets
st1.update(st2)
print(st1)

# finding common items or intersections
print(st1.intersection(st2))

# checking subset and superset
print(st2.issubset(st1))
print(st2.issuperset(st2))

# checking diffrence between two set
print(st1.difference(st2))
print(st2.symmetric_difference(st1)) #gives the set that contains all items from both set except for the same items contains
print(st1.symmetric_difference(st2))

# joint and disjoint set
st1={1,2,3,4}
st2={1,2,3,4,5,6,7,8}
st3={'a','v','c'}

print(st1.isdisjoint(st2)) #false cause has common items
print(st2.isdisjoint(st1)) #false cause has common items
print(st1.isdisjoint(st3)) #True cause has no common items
