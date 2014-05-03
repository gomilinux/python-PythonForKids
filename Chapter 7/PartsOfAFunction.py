#Python for Kids Chapter 7 Recycling Your Code With Functions and Modules
#Functions have three parts: name, parameter, body


def testfunc(myname):
	print('hello %s' % myname)
	
testfunc('Mary')

def testfunc2(fname, lname):
	print('hello %s %s' % (fname, lname))
	
testfunc2('Mary', 'Smith')

firstname = 'Joe'
lastname = 'Robertson'

testfunc2(firstname, lastname)

def savings(pocket_money, paper_route, spending):
	return pocket_money + paper_route - spending

print(savings(10, 10, 5))


def variable_test():
	first_variable = 10
	second_variable = 20
	return first_variable * second_variable

print(variable_test())

#print(first_variable)

def variable_test(first_variable, second_variable):
	return first_variable * second_variable
	
print(variable_test(20, 30))

another_variable = 100
def variable_test():
	first_variable = 10
	second_variable = 20
	return first_variable * second_variable * another_variable
	

print(variable_test())
print(another_variable)

def spaceship_building(cans):
	total_cans = 0
	for week in range(1, 53):
		total_cans = total_cans + cans
		print('Week %s = %s cans' % (week, total_cans))

spaceship_building(2)


