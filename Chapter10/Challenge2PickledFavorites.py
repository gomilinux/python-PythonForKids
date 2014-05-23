#Python For Kids
#Chapter 10
#Challenge 2 Pickled Favorites

import pickle

my_favorites = ['Dr. Who', 'Battlestar Galactica', 'One Piece', 'Samurai X', 'Ghost in the Shell', 'Attack on Titan']

save_file = open('favorites.dat', 'wb')
pickle.dump(my_favorites, save_file)
save_file.close()

load_file = open('favorites.dat','rb')
loaded_favorites = pickle.load(load_file)
load_file.close()

print(loaded_favorites)

