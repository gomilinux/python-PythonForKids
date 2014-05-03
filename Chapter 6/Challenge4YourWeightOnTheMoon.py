#Python For Kids Chapter 6 Challenge 4 Your Weight On The Moon
#Calculate weight on moon using 0.165. If you gained a kilo in weight every
#year for the next 15 years, what would your weight be at the end of the 15 years?

weight = 155
year = 1

for x in range(1,16):
	new_weight = (weight + (x-1))*0.165 
	print("Year %s" % x + " = " + str(new_weight))
	
print (155+14)*0.165

