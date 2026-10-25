# Exercise1
#import random
#random_ = random.random()
#for i in range(10):
#    print(random_)

#Exercise2
#import random
#for i in range(10):
#    randomt = random.randrange(25,36)

#    print(randomt)

#Exercise3

#import math
#side1 = int(input("Enter side 1: "))
#side2 = int(input("Enter side 2: "))
#hypotenuse = math.hypot(side1 ,side2 )
#print("The hypotenuse is: ",hypotenuse)

#Exercise4

#import math

#area = int(input("Enter the area of the circle: "))
#radius = (area / math.pi) ** 0.5
#print("the radius of the circle is:", radius)

#Exercise5

#import turtle

#wn = turtle.Screen()
#tae = turtle.Turtle()

#for i in range(5):
#    tae.forward(100)
#    tae.right(144)

#wn.exitonclick()

#Exercise6

#import turtle

#def drawSquare(t,sz):
#    for i in range(4):
#        t.forward(sz)
 #       t.left(90)

#wn = turtle.Screen()
#wn.bgcolor("lightgreen")
#tae = turtle.Turtle()
#tae.pensize(3)
#tae.color("hotpink")

#for i in range(5):
#    drawSquare(tae,20)
#    tae.penup()
#    tae.forward(40)
#    tae.pendown()
#wn.exitonclick()

#Exercise7

#import turtle

#def drawSquare(t, size):
#    for i in range(4):
#        t.fd(size)
#        t.lt(90)


#wn = turtle.Screen()
#wn.bgcolor("lightgreen")
#tae = turtle.Turtle()
#tae.pensize(3)
#tae.color("hotpink")

#size = 20

#for i in range(5):
#    drawSquare(tae, size)
#    tae.penup()
#    tae.backward(10)
#    tae.right(90)
#    tae.forward(10)
#    tae.left(90)
#    tae.pendown()
#    size = size + 20
#wn.exitonclick()



