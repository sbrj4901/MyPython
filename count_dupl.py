# method1
l = ['a','b','c','d','a','b','c']
duplicate = {}
for i in l:
	duplicate[i] = l.count(i)
print(duplicate)

# method2
l = ['a','b','c','d','a','b','c']
b = {}
for i in l:
	if i not in b:
		b[i]  =1
	else:
		b[i] += 1
print(b)
# method3
from collections import Counter
l = ['a','b','c','d','a','b','c']
b = Counter(l)
print(b)

