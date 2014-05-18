#Python for Kids Chapter 7 Challenge 1 Basic Moon Weight Function
#Create a function that takes a starting weight and increases the weight amount each year.
#Calculate for different periods such as 5 years or 20 years.

import sys

weight = 0
increase = 0
period = 0
def moon_weight(weight, increase, period):
	print('What is your weight?')
	weight = int(sys.stdin.readline())
	print('How much does your weight increase each year?')
	increase = int(sys.stdin.readline())
	print('For how many years?')
	period = int(sys.stdin.readline())		
	for x in range(1,period+1):
			new_weight = (weight + ((x)*increase))*0.165 
			print("Year %s" % x + " = " + str(new_weight))
			
moon_weight(weight, increase, period)

