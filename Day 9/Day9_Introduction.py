# Conditional Statement
# if condition
a=0
if a > 0:
    print('A is a positive number')
elif a<0:
    print('A is a negative number')
else:
    print('A = 0')

# short Hand Method
b= "Sanyam"
print('b is a string value') if isinstance(b,str) else print('b is not a string value')

# nested Condition
a=5

if a > 0:
    if a%2==0:
        print('A is a positive number and also even number')
    else:
        print('A is a positive number and also odd number')
elif a==0:
    print('A is zero')
else:
    print('A is a negative nummber')

# Using operators for simpler neseted method
a=5

if a>0 and a%2==0:
    print('A is positive and even number')
elif a>0 and a%2!=0:
    print('A is positive and odd number')
elif a==0:
    print('A is zero')
else:
    print('A is a negative number')

# OR operator
user='admin'
access_level =3
if user=='admin' or access_level>=4:
    print('Access Granted')
else:
    print('Acess Denied')       
    