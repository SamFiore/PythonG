import turtle

point = turtle.Turtle()

for i in range(0,4):
    #Posición en la que se movería.
    point.forward(100)
    #Grados en los que se movería.
    point.left(90)

for i in range (0,4):
    point.forward(-100)
    point.left(-90)

point.left (90)
point.forward(100)
point.left (-90)
point.forward(-50)
point.left(90)
point.forward(200)
point.left(-90)
point.forward(100)
point.left(90)
point.forward(-200)
point.left(-90)
