#Python For Kids
#Chapter 10
#Load a pickle saved file


import pickle
load_file = open('save.dat', 'rb')
loaded_game_data = pickle.load(load_file)
load_file.close()

print(loaded_game_data)