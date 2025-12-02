# Writ a function which generates a six digit/character random_user_id.

import mymodule
print(mymodule.random_user_id(6))

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
#  One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# print(mymodule.user_id_gen_by_user())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

print(mymodule.rgb_color_gen())

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

print(mymodule.list_of_hexa_colors(4))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

print(mymodule.list_of_rgb_colors(3))

# Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

print(mymodule.generate_colors('hexa',3))
print(mymodule.generate_colors('hexa',1))
print(mymodule.generate_colors('rgb',3))
print(mymodule.generate_colors('rgb',1))

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

print(mymodule.shuffle_list([1,2,3,4,5]))
print(mymodule.shuffle_list([1,'a',3,'b',5]))
print(mymodule.shuffle_list(['a','b','c','d','e']))

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

print(mymodule.unique_number())