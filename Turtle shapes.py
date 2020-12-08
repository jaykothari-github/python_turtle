# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:36:00 2020

@author: HP
"""

import turtle

a = 5
print(a)

jay_turtle = turtle.Turtle()
jay_turtle.speed(30) #Speed control
#jay_turtle.anglespeed(40)

#square()

'''def square():
  jay_turtle.forward(100)
  jay_turtle.right(90)
  jay_turtle.forward(100)
  jay_turtle.right(90)
  jay_turtle.forward(100)
  jay_turtle.right(90)
  jay_turtle.forward(100)

square()
jay_turtle.forward(50)
square()
jay_turtle.forward(50)
square()
jay_turtle.forward(50)
square()
jay_turtle.forward(50)'''

#Circle

def circle():
  for count in range(360):
    jay_turtle.forward(1)
    jay_turtle.right(1)
    
  for count in range(360):
    jay_turtle.forward(1)
    jay_turtle.left(1)
  

jay_turtle.speed(100)
for count in range(72):
  circle()
  jay_turtle.right(5) 


#Triangle

'''def Triangle():
  jay_turtle.forward(100)
  jay_turtle.left(120)
  jay_turtle.forward(100)
  jay_turtle.left(120)
  jay_turtle.forward(100)

Triangle()'''