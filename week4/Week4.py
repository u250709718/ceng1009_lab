#Exercise1

#for i in range(100):
#   print("we like python's turtle!")

#Exercise2
#for month in ["January","February","March","April","May","June","July","August","September","October","November","December"]:
#    print("One of the months of the year is", month)

#Exercise3
#for i in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
#    print(i, i ** 2)

#Exercise4

#import turtle

#wn = turtle.Screen()
#tae = turtle.Turtle()

#for i in range(3):
#    tae.forward(100)
#    tae.left(120)

#for i in range(4):
#    tae.forward(100)
#    tae.left(90)

#for i in range(6):
#    tae.forward(100)
#    tae.left(60)

#for i in range(8):
#    tae.forward(100)
#    tae.left(45)

#wn.exitonclick()

#Exercise5
#side = int(input("Enter side: "))
#lenght = int(input("Enter length: "))
#color = input("Enter the sidecolor: ")
#fillcolor = input("Enter the fillcolor: ")

#angle = 360 / side

#import turtle
#wn = turtle.Screen()
#tae = turtle.Turtle()
#tae.speed(100)
#tae.color(color)
#tae.fillcolor(fillcolor)

#tae.begin_fill()

#for i in range(side):
#    tae.forward(lenght)
#    tae.left(angle)
#tae.end_fill()
#wn.exitonclick()

#Exercise6
#import turtle
#wn = turtle.Screen()
#tae = turtle.Turtle()

#for angle in [160,-43, 270,-97,-43, 200,-940, 17,-86]:
 #   tae.right(angle)
 #   tae.forward(100)

#wn.exitonclick()

#Exercise7
#import turtle
#wn = turtle.Screen()
#tae = turtle.Turtle()

#for i in range(5):
#    tae.forward(100)
#    tae.right(144)

#wn.exitonclick()

#Exercise8
#import turtle
#wn = turtle.Screen()
#wn.bgcolor("lightgreen")
#tae = turtle.Turtle()
#tae.color("blue")
#tae.shape("turtle")
#tae.penup()
#for i in range(12):
#    tae.forward(80)
#    tae.pendown()
#    tae.forward(15)
#    tae.penup()
#    tae.forward(15)
#    tae.stamp()
#    tae.backward(110)
#    tae.right(30)
#wn.exitonclick()

#Exercise9
#legs = int(input("Enter number of legs: "))
#angle = 360 / legs

#import turtle
#wn = turtle.Screen()
#tae = turtle.Turtle()

#for i in range(legs):
#    tae.forward(100)
#    tae.backward(100)
#    tae.left(angle)

#wn.exitonclick()

