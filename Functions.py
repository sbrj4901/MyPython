# FUNCTIONS
# Inbuild function[zip]
l1=[1,2,3,4]
l2=[4,5,6,7]
for a,b in zip(l1,l2):
	print(a,b)
l1=['sachin','kohli','ishant']
l2=['batsman','batsman','bowler']
print(list(zip(l1,l2)))
c=dict()
for a,b in zip(l1,l2):
	c[a]=b
print(c)


	
	