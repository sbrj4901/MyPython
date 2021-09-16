class Calculator():
		def addtion(self, a, b):
			c = a + b
			return c
		def subraction(self, a, b):
			c = a - b
			return c
		def multiply(self, a, b):
			c = a * b 
			return c
		def divide(self, a, b):
			c = round(a / b)
			return c

s = Calculator()
a = s.addtion(10,2)
b = s.subraction(20,3)
c = s.multiply(50,20)
d = s.divide(20,10)
print(a)
print(b)
print(c)
print(d)
