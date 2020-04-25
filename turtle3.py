import turtle

bob= turtle.Turtle()
bob.getscreen().bgcolor("red")


#for i in range(5):
#    bob.forward(10)
#    bob.left(216)
bob.penup()
bob.goto((-200,100))
bob.pendown()
def star(turtle,size):
    if size <=10:
        return
    else:
        for i in range(5):
           turtle.forward(10)
           size(turtle , int(size/2))
           turtle.left(216)

star(bob , 100)


turtle.done()