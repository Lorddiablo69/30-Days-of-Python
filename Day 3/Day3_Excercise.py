age= 24
height= 5.5
complex= 3 + 2j

# Calculating area of triangle
base= int(input("Enter base of the triangle: "))
height= int(input("Enter height of the triangle: "))
area_triangle= 0.5 * base * height
print("The area of the triangle is:", area_triangle)

# Calculating perimeter of triangle
side_a= int(input("Enter side a of the triangle: "))
side_b= int(input("Enter side b of the triangle: "))
side_c= int(input("Enter side c of the triangle: "))
perimeter_triangle= side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter_triangle)

# calculating area of rectangle
length= int(input("Enter length of the rectangle: "))
width= int(input("Enter width of the rectangle: "))
area_rectangle= length * width
perimeter_rectangle= 2 * (length + width)
print("The area of the rectangle is:", area_rectangle)
print("The perimeter of the rectangle is:", perimeter_rectangle)

# calculating area of circle
radius= int(input("Enter radius of the circle: "))
area_circle= 3.14 * radius**2
circumference_circle= 2 * 3.14 * radius
print("The area of the circle is:", area_circle)
print("The circumference of the circle is:", circumference_circle)

# Calculate the slope of y=2x-2

x1=2
y1= 2
x2=6
y2=10
m= (y2 - y1) / (x2 - x1) # m is the slope
print("The slope of the line is:", m)

# calcualte the value of y
# y= x**2 + 6*x + 9
# y=(x + 3)*(x + 3)
# when y is 0
x= -3
print("The value of x when y is 0 is:", x)

# False comparison
print(len('python') == len('dragon'))
print(len('python') != len('dragon'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'python' and 'on' not in 'dragon')
print(len('pyhton'), float(len('python')), str(len('python')))

# checking if number is even or odd
number= int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")

# floor division
print((7 // 3)== int(2.7))
print('10' == 10)
print(int('9.8') == 10)

# Calculate weekly earning
hours= int(input("Enter hours: "))
rate_per_hour= int(input("Enter rate per hour: "))
pay= hours * rate_per_hour
print("Your weekly earning is:", pay)

# Calculate number of seconds lived
numbers_of_years= int(input("Enter number of years you live: "))
seconds= numbers_of_years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds")

# print table
for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")
