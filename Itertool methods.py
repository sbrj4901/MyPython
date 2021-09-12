import itertools
print(dir(itertools))
L1=['Apple','Orange','Pineapple','Banana','Jackfruit','Cherry','Plums','Lemon','Papaya','Fig']
L2=['Bata','Adidas','Puma','Woodland','Paragon']
c=dict()
for a,b in itertools.zip_longest(L1,L2):
	c[a]=b
print(c)
# print(dir(itertools))
