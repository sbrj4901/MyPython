# return statement examples
def add(a, b):
	return a + b

def is_true(a):
	return bool(a)
a = add(4, 2)
print('result of add function is ',(a))

b = is_true(2 < 5)
print('result of is_true function is',(b))

#method using tuple
def fun():
	str = 'Python'
	x = 30
	return str, x
str, x = fun ()
print(str)
print(x)

#method using list
def fun():
	str = 'Python'
	x = 30
	return [str, x]
list = fun()
print(list)

#method using dictionary
def fun():
	d = dict()
	d ['str'] = "geeks for geeks"
	d ['x'] = 20
	return d
d = fun()
print(d)
