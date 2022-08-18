#!/usr/bin/env python3.10

import turtle
import os
import _tkinter as tk

wn = turtle.Screen()
wn.title("Pong by @Garrett")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#Function
def paddle_a_up():
    y= paddle_a.ycor()
    y =+ 20
    paddle_a.sety(y)

#Keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")

# Main Game Loop
while True:
    wn.update()