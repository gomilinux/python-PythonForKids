#Python For Kids Chapter 10
#Time Module

import time

#print(time.time())

def lots_of_numbers(max):
	t1 = time.time()
	for x in range(0, max):
		print(x)
	t2 = time.time()
	
	print('It took %s seconds.' % (t2-t1))	
lots_of_numbers(1000)		


#Convert to readable Date and Time

print(time.asctime())

#Date-time format using a tuple
#year, month, day, hours, minutes, seconds, day of the week, day of the year, daylight saving time

t = (2007, 5, 27, 10, 30, 48, 6, 0, 0)

print(time.asctime(t))

print(time.localtime())

t = time.localtime()
year = t[0]
month = t[1]
print(year)
print(month)

