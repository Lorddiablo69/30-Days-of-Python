# creating empty tuple
tp1=()

sister=('sis1','sis2','sis3')
brother=('bro1','bro2','bro3')
siblings=sister+brother
print(siblings)
print(len(siblings))
modify=list(siblings)
modify.append('father1')
modify.append('mother1')
print(modify)
family_member=modify

fruits=('apple','banana','orange')
vegetables=('potato','onion','spinach')
animal_products=('butter','milk','meat')
food_stuff_tp=fruits+vegetables+animal_products
food_stuff_It=list(food_stuff_tp)
print(food_stuff_It[len(food_stuff_It)//2])
print(food_stuff_It[0:3])
print(food_stuff_It[-3:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries)
