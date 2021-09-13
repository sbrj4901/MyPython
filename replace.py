# Replace.py
a='Hello world'
c=a.replace('world','universe')
print(c)

greetings='Hello'
name='michael'
a='{},{} welcome!'.format(greetings,name)
print(a)
# # instead
a=f'{greetings},{name.upper()} welcome!'
print(a)
print(help(str.lower))
l1=['sachin','kohli','ishant']
l2=['batsman','batsman','bowler']
