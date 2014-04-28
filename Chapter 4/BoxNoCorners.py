#box without corners

import turtle

t = turtle.Pen()
count = 0

while count < 4:

	#one side
	t.up()
	t.forward(50)
	t.down()
	t.forward(100)
	t.up()
	t.forward(50)

	t.left(90)
	count = count + 1




turtle.done()