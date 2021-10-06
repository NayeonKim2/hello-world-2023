from turtle import *
import random

penup()
hideturtle()

bgcolor("black")
color("pink")
speed(0.1)

setposition(-305,290)
pendown()

def changeColor():
    R = random.random()
    G = random.random()
    B = random.random()

    color(R, G, B)

def roseDraw():
    for i in range (35):
        forward(i*0.8)
        right (68)
    setheading(0)

def roseFirst():
    penup()
    changeColor()
    setposition(xcor()+80, ycor()+25)
    pendown()

def roseSecond():
    penup()
    changeColor()
    setposition(xcor()-80, ycor()+25)
    pendown()



for i in range (9):
    roseDraw()
    roseFirst()

setheading(0)
penup()
goto(xcor(), ycor()-80)
pendown()

for i in range (9):
    roseDraw()
    roseSecond()

setheading(0)
penup()
goto(xcor()+70, ycor()-80)
pendown()

for i in range(9):
    roseDraw()
    roseFirst()

setheading(0)
penup()
goto(xcor(), ycor()-80)
pendown()

for i in range (9):
    roseDraw()
    roseSecond()

setheading(0)
penup()
goto(xcor()+70, ycor()-80)
pendown()

for i in range(9):
    roseDraw()
    roseFirst()
    
setheading(0)
penup()
goto(xcor(), ycor()-80)
pendown()

for i in range (9):
    roseDraw()
    roseSecond()

setheading(0)
penup()
goto(xcor()+70, ycor()-80)
pendown()

for i in range(9):
    roseDraw()
    roseFirst()
    
setheading(0)
penup()
goto(xcor(), ycor()-80)
pendown()

for i in range (9):
    roseDraw()
    roseSecond()

setheading(0)
penup()
goto(xcor()+70, ycor()-80)
pendown()

for i in range(9):
    roseDraw()
    roseFirst()

done()