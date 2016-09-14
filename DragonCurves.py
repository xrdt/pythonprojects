#this is a dragon curve demonstration implemented through Turtle
import turtle

turtle

iter = int(raw_input("Please enter the number of iterations"
					 " you would like to see: "))

old = 'r'

cycle = 1

while cycle <= iter:
	oldrev = old[::-1]
	for char in range(0, len(old)):
		if oldrev[char] == 'r':
			oldrev = oldrev[:char] + 'l' + oldrev[char+1:] 
		else:
			oldrev = oldrev[:char] + 'r' + oldrev[char+1:]

	new = old + 'r' + oldrev 
		 
	turtle.pendown()
	turtle.color("black")
	turtle.pensize(3)

	for char in range(0, len(new)):
		if new[char] == 'r':
			turtle.right(90)
			turtle.forward(20)
		if new[char] == 'l':
			turtle.left(90)
			turtle.forward(20)
	
	old = new
	cycle += 1

turtle.exitonclick()
