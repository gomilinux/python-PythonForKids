#Python For Kids Chapter 10 Useful Python Modules
class Animal:
	def __init__(self, species, number_of_legs, color):
		self.species = species
		self.number_of_legs = number_of_legs
		self.color = color
		
harry = Animal('hippogrif', 6, 'pink')

import copy

harriet = copy.copy(harry)

print('Harry is a ' + harry.species + '.')

print('Harriet is a ' + harriet.species + '.')

carrie = Animal('chimera', 4, 'green polka dots')
billy = Animal('bogilla', 0, 'paisley')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)

my_animals[0].species = 'ghoul'

print(more_animals[0].species)
print(more_animals[1].species)

print(my_animals[0].species)
print(more_animals[0].species)

sally = Animal('sphinx', 4, 'sand')
my_animals.append(sally)

print('animals' + '=' + str(len(my_animals)))

print('more_animals' + '=' + str(len(more_animals)))


