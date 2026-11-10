import turtle

t = turtle.Turtle()
t.pensize(3)
t.color("cyan")
for j in range(12):      
    for i in range(6):      
        t.forward(100)
        t.left(60)        
    t.left(30)
turtle.done()