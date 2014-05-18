#Python for Kids Chapte 9

print(max(2, 49, 9823, 489283, 8342))

print(min(2, 49, 9823, 489283, 8342))

numbers = [23, 3, 25, 263, 243, 24266, 34,]

print(min(numbers))

guess_this_number = 61
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
	print('Boom! You all lose')
else:
	print('You win')
	
for x in range(1, 11):
	print(x)


print(list(range(0, 5)))

count_down_by_twos = list(range(0, 40, 2))
print(count_down_by_twos)

count_down_by_twos = list(range(40, 10, -2))
print(count_down_by_twos)

my_list_of_numbers = list(range(0, 500, 50))
print(sum(my_list_of_numbers))

