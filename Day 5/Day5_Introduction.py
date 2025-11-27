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
# Inserting elements at a specific position
lst.insert(1,'shakya')
print(lst)
# Removing elements from a list
lst.remove(45)
print(lst)
# Popping elements from a list
print(lst.pop()) #removes last item of index
print(lst)
print(lst.pop(2))
print(lst)
# removing using Del
lst=['sanyam', 'shakya', 45, False, {'name': 'sanyam'}, (1, 2, 3), {'age': 21}]
del lst[2]
print(lst)
del lst #delete lists completely
# Clearing list
lst=['sanyam', 'shakya', 45, False, {'name': 'sanyam'}, (1, 2, 3), {'age': 21}]
lst.clear()
print(lst)
# copying list
lst=['sanyam', 'shakya', 45, False, {'name': 'sanyam'}, (1, 2, 3), {'age': 21}]
lst_copy=lst.copy()
print(lst_copy)
# joining lists
# plus operator
positive=[1,2,3]
negative=[-1,-2,-3]
zero=[0]
print(positive+zero+negative)
# extend method
positive.extend(negative)
print(positive)
# count method
print(positive.count(-3))
# indexing
print(positive.index(-1))
# reversing
positive.reverse()
print(positive)
# sorting
order=['a','b','c','e','f','d','g','h']
order.sort() #ascending order
print(order)
order.sort(reverse=True) #descending order
print(order)
# sorted it returns the orderes list without changing the original list
order2=[1,4,6,8,2,9,3,10,5]
print(sorted(order2)) #ascending order
print(sorted(order2,reverse=True)) #descending order
print(order2) #unchanged list
