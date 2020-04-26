import turtle
my_turtle=turtle.Turtle()
my_turtle.speed(1)
c1=['green']
def drawArt(d,angle,x,y):
    my_turtle.up()
    my_turtle.goto(x,y)
    my_turtle.down()
    for i in range(0,400):
        my_turtle.pencolor(c1[0])
        my_turtle.forward(d)
        my_turtle.left(angle)
        d=d-1
        
drawArt(50,50,0,0)
