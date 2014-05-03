#Python For Kids Magic Coins For Loop

found_coins = 20  #coins found a week
magic_coins = 70  #magic coins = 10 magic coins a day or 70 a week
stolen_coins = 3  #coins stolen by raven a week

coins = found_coins
for week in range(1, 53): 
	coins = coins + magic_coins - stolen_coins
	print('Week %s = %s' % (week, coins))
	
