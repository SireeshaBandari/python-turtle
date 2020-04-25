import turtle
import math
import random
 
bob = turtle.Turtle()
bob.color("blue" , "green")
bob.speed(10)

bob.begin_fill()
for i in range(100):
      bob.forward(100)#sin(i/10)*25
      bob.left(170)#try i%90
bob.end_fill()

turtle.done()