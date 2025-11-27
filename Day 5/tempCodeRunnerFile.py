# Introduction to lists in Python
# creatingg list
lst=list()
lst=[]
lst=['sanyam',45,True,{'name':'sanyam'},(1,2,3)]

# Accessing list elements
print(lst[3])          # {'name':'sanyam'}
print(lst[-1])         # (1,2,3)
# Slicing lists
print(lst[1::3])
print(lst[::2])
print(lst[0:])
print(lst[:-1])
print(lst[::-1])
# Modifying list elements
lst[2]=False
print(lst)
# Checking list items
exist='sanyam'in lst
print(exist)        # True
# Adding elements to a list
lst.append({'age':21})
print(lst)
