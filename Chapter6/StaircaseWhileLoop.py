#Python for Kids Chapter 6 Staircase While Loop

for step in range(0, 20):
	print(step)
	


step = 0 
tired = False
badweather = False
while step < 10000:
	print(step)
	if tired == True:
		break
	elif badweather == True:
		break
	else:
		step = step + 1
		

x = 45
y = 80

while x < 50 and y < 100:
	x = x + 1
	y = y + 1
	print(x, y)
	
