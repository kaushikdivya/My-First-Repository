##Animal is-a object
class Animal(object):
	pass

##
class Dog(Animal):
	
	def __init__(self, name):
		self.name = name
		print "Dog", name
		
##
class Cat(Animal):

	def __init__(self, name):
		self.name = name
		print "Cat", name
		
##
class Person(object):

	def __init__(self, name):
		self.name = name
		self.pet = None
		print "Person name" , name
		print "Person pet", self.pet
		
##
class Employee(Person):

	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary
		print "employee", name
		print "salary", salary
		
class Fish(object):
	pass
	
class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan
Divya = Person("Divya")
Divya.pet = "Furry"
print "Divya pet", Divya.pet
print "mary pet", mary.pet

frank = Employee("Frank", 120000)

frank.pet = rover
print "frank pet", frank.pet


flipper = Fish()

crouse = Salmon()

harry = Halibut()

