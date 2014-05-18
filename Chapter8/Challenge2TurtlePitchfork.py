#Python For Kids Chapter 8 Challenge #2 Turtle Pitchfork
#Use turtle objects and move them around to create a sideways pitchfork

import turtle

#handle = turtle.Pen()
topfork1 = turtle.Pen()
topfork2 = turtle.Pen()
bottomfork1 = turtle.Pen()
bottomfork2 = turtle.Pen()


topfork1.forward(150)
bottomfork1.forward(150)

topfork1.left(90)
bottomfork1.right(90)
topfork1.forward(80)
bottomfork1.forward(80)

topfork2.forward(200)
bottomfork2.forward(200)

topfork2.left(90)
bottomfork2.right(90)

topfork2.forward(40)
bottomfork2.forward(40)


topfork1.right(90)
bottomfork1.left(90)
topfork2.right(90)
bottomfork2.left(90)


topfork1.forward(90)
bottomfork1.forward(90)
topfork2.forward(40)
bottomfork2.forward(40)


turtle.exitonclick()
