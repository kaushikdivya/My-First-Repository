class Parent(object):
	def overwrite(self):
		print "Parent overwrite"
		
class Child(Parent):

	def __init__(self):
		self.rock = Parent()
	def overwrite(self):
		super(Child, self).overwrite()
		print "Child overwrite"
		
		
dad = Parent()
son = Child()

dad.overwrite()
son.overwrite()
print son.rock
print isinstance(dad, Parent)
print hasattr(son, 'rock')