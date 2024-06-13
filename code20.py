# Write a function called square that takes a parameter named t, which is a turtle. 
# It should use the turtle to draw a square


import turtle

def square(t):
    for _ in range(4):
        t.forward(100)
        t.right(90)

my_turtle = turtle.Turtle()
square(my_turtle)
turtle.done()


# Write a function call that passes bob as an arguement to square, and then run the program again

bob = turtle.Turtle()

square(bob)

turtle.mainloop()
