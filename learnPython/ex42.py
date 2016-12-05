#animal is a object 
class Animal (object):
	pass 
	
	# dog is an anaimal 
class Dog(Animal):
	
	def __init__(self,name): 
	# dog has a name
		self.name = name 
	
	
	# cat is animal 
class Cat(Animal):

	def __init__(self, name):
	# cat has a name
		self.name = name
	

# person is an object 
class Person(object):

	names=[]
	def __init__(self, name):
	# person has a name 
		self.name = name
	
	#person has a pet of somekind 
		self.pet = None
	def add_name(self):
		self.names.append(self.name)
	
	#employee is a person
class Employee(Person):
	
		def __init__(self, name, salary):
			
			super(Employee, self).__init__(name)
			
			self.salar = salary
			

## class fish is an object 
class Fish(object):

	pass
	
class Hib(Fish):

	pass
	
class  Samon(Fish):

	pass

class Dogs_test:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
	
##rover is a dog 
rover = Dog("rover")
## satan is a cat
satan = Cat("satan")
## mary si a person
mary = Person("mary")
rom = Person ("tom")
mary.add_name()
rom.add_name()

print mary.names
##mary has a pet 
#mary.pet = rover
mary.pet = rover.name

#frank is an employee 
frank = Employee("frank", 120000)
frank.pet = satan

flipper = Fish()

course = Samon()

	

print rover.name
print mary.name, mary.pet






