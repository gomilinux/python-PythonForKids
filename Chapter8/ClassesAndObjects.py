#Kids for Python Chapter 8 How to Use Classes and Objects

class Things:
	pass
	
class Inanimate(Things):
	pass
	
class Animate(Things):
	pass
	
class Sidewalks(Inanimate):
	pass
	
class Animals(Animate):
	pass

class Mammals(Animals):
	pass
	
class Giraffes(Mammals):
	pass
	


#Adding characteristics to classes. A characteristic is a trait that all members of the class and children share. Characteristics can be thought of as functions or things that an object of that class can do.

class Animals(Animate):
	def breathe(self):
		print('breathing')
	def move(self):
		print('moving')
	def eat_food(self):
		print('eating food')


class Mammals(Animals):
	def feed_young_with_milk(self):
		print('feeding young')

class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print('eating leaves')

#Call functions to on object by using the dot operator and the name of the function.

reginald = Giraffes()
harold = Giraffes()
reginald.move()
harold.eat_leaves_from_trees()




