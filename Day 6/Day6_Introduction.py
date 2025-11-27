# Introuction to tuples
# Tuples are not mutable because we cannot modify its data
empty_tuple=()
tuple1=('item1','item2','item3','item4')
print(len(tuple1))

# Accessing Tuple
print(tuple1[0])

# Slicing Tuple
print(tuple1[1:2])

# To change the data of tuples you have to change it to list first then only we can change it 
lst=list(tuple1)
print(lst)

# Checking item in tuple
print('item1'in tuple1)

# joining tuple
tp1=('sanyam','shakya','class')
tp2=('nepal','trick','facebook')
tp3=tp1+tp2
print(tp3)

# deleteing tuple
del tp3