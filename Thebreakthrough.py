import turtle 
# Creates a screen with a light green background and title of #Turtle
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")

#Creating a couple of objects for easier functionality
square = turtle.Turtle()
star = turtle.Turtle()

#Draw a square 
for i in range(4):
    square.forward(200)
    square.left(90)

#Draw a star
star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

turtle.done()







