#Python For Kids
#Chapter 10
#Using pickle module

import pickle

game_data = {
	'player postion' : 'N23 E45',
	'pockets' : ['keys', 'pocket knife', 'polished stone'],
	'backpack' : ['rope', 'hammer', 'apple'],
	'money' : 158.50
}


save_file = open('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()

