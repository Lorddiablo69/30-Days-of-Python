# empty list

lst=[]

# list with 5 items

lst=[2,4,5,3,1]
print(len(lst))
print(lst[0],lst[2],lst[4])

# modifying the list

it_company=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_company)
print(len(it_company))
print(it_company[0],it_company[3],it_company[6])
it_company[4]='TikTok'
print(it_company)
it_company.append('IBM')
print(it_company)
it_company.insert(3,'Spotify')
print(it_company)
it_company[2]=it_company[2].upper()
print(it_company)
new_string=['#; ']
it_company=it_company+new_string
print(it_company)
exist='IBM' in it_company
print(exist)
it_company.sort()
print(it_company)
it_company.reverse()
print(it_company)
print(it_company[0:3])
print(it_company[-3:])
del(it_company[0])
print(it_company)
del(it_company[4])
print(it_company)
del(it_company[-1])
print(it_company)
del(it_company)

#joining the list and inserting the elements 

front_end=['HTML','CSS','JS','React','Redux']
back_end=['Node','Express','MongoDB']
joining=front_end+back_end
print(joining)
full_stack=joining.copy()
print(full_stack)
full_stack.insert(5,'Python')
full_stack.insert(5,'SQL')
print(full_stack)

# Excercise 2

ages=[19,22,19,24,20,25,26,24,25,24]

# sorting

ages.sort()
print(ages)
ages.append(min(ages))
ages.append(max(ages))
ages.sort()
print(ages)
print(len(ages))
median=(ages[5]+ages[6])/2
average=sum(ages)/len(ages)
ranges=max(ages)-min(ages)
minium=min(ages)-average
maximum=max(ages)-average
print(f'The median is {median} and the average of the list is {average} and the range is {ranges} \nand the min and max values are {minium} and {maximum} respectively')

# Countires

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# middle country
print(countries[len(countries)//2])
# dividing countries list in half
first_half=countries[:(len(countries)//2)+1]
second_half=countries[(len(countries)//2)+1:]
print(first_half,second_half)

unpack=['China','Russia','USA',"Finland",'Sweden','Norway','Denmark']
first=unpack.pop(0)
second=unpack.pop(0)
third=unpack.pop(0)
scandic=unpack
print(f'Unpacked first three countries are {first},{second},{third} and the rest of the list are {scandic}')