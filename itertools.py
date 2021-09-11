from itertools import groupby
# print(dir(itertools))
L1=[
{
"Name":"Venkat",
"Age":25,
"City":"Chennai",
"Nationality":"india"
},
{
 "Name":"Arun",
 "Age":23,
 "City":"Madurai",
 "Nationality":"India"
},
{
"Name":"Karthick",
"Age":24,
"City":"Salem",
"Nationality":"India"
},
{
"Name":"Sankar",
"Age":28,
"City":"Chennai",
"Nationality":"India"
},
{
"Name":"Ram",
"Age":25,
"City":"Chennai",
"Nationality":"India"
},
{
"Name":"Kishore",
"Age":27,
"City":"Salem",
"Nationality":"India"
},
{
"Name":"Selva",
"Age":25,
"City":"Chennai",
"Nationality":"India"
},
{
"Name":"Rajesh",
"Age":28,
"City":"Tuticorin",
"Nationality":"India"
},
{
"Name":"Kumar",
"Age":27,
"City":"Chennai",
"Nationality":"India"
},
{
"Name":"Aravind",
"Age":26,
"City":"Salem",
"Nationality":"India"
}
]
def key_func(b):
	return b['City']
L1=sorted(L1,key=key_func)
for key,value in groupby(L1,key_func):
	print(key)
	print(list(value))
	# for data in (value):
	# 	print(data)

































