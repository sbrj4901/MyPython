#Day9 functions
l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]

def union(a,b):
	c = list(set(a).union(b))
	print(c)
union(l1,l2)



def msg():
	d = 10
	print('The value of d is',d)
	# return
msg()
# print(d)