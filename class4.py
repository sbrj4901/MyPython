class Employee:
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

		
class Developer(Employee):
	def __init__(self, name, age, salary, Programminglanguage):
		
		 Employee.__init__(self, name, age, salary )
		 self.Programminglanguage = Programminglanguage
a= Developer("subaraj",28,28000,'Python')
print(a.name, a.age, a.salary, a.Programminglanguage)

