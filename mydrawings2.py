import turtle
turtle.title('This is for you Dante')
turtle.setworldcoordinates(-2000,-2000,2000,2000)

def Dante(x,y,tilt,radius):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)
    
for tilt in range(0,360,30):
    Dante(0,0,tilt,1000)