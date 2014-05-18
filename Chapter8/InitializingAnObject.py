#Kids for Python Chapter 8 How to Use Classes and Objects
#Initializing an Object
# The init funtion is __init__

class Giraffes:
	def __init__(self, spots):
		self.giraffe_spots = spots
		

ozwald = Giraffes(100)
gertrude = Giraffes(150)

print(ozwald.giraffe_spots)

print(gertrude.giraffe_spots)

