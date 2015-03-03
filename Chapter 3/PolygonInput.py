n = int(input("Define the number of sides greater than 2 that you would like for your polygon: "))

import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.goto(-100,-100)
t.pendown()

if n > 2:
	for i in range(n+1):
		angle = 180 - (((n-2)*180)/n)
		t.forward(50)
		t.left(angle)
else:
	print("The number of sides must be greater than 2.")
	
input()