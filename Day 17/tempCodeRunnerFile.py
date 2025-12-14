
fruits=['apple','banana','mango','orange','kiwi']
veg=['potato','onion','tomato','carrot']
combine=[]
for f,v in zip(fruits,veg):
    combine.append({'fruits':f,"veg":v})
print(combine)
