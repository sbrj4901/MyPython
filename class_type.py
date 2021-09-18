#class type example
class Laptop:
	
	def __init__(self, name, processor, hdd, ram, cost):
		self.name = name
		self.processor = processor
		self.hdd = hdd
		self.ram = ram
		self.cost = cost
		
	def details(self):
		print('The details of the laptop are:')
		print('Name         :', self.name)
		print('Processor    :', self.processor)
		print('HDD Capacity :', self.hdd)
		print('RAM          :', self.ram)
		print('Cost($)      :', self.cost)
		
#create object
laptop1 = Laptop('Dell Alienware', 'Intel Core i7', 512, 8, 2500.00)

print(laptop1.name)
print(laptop1.processor)

laptop1.details()