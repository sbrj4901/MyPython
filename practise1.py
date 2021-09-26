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

#return multiple values from a method using class 
class Test:
 	def __init__ (self):
 		self.str ='geeks for geeks'
 		self.x = 20

def fun():
	return Test()
a = fun()
print(a.str)
print(a.x)

#Python User Defined Function
def calculate_si_amount(principal, rate, time):
  interest =  (principal*rate*time)/100
  return principal+interest
print (calculate_si_amount(9,10,4))