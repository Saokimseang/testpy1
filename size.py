import turtle

# Get the size of the square/rectangle from the user
size = int(input("What size should the rectangle be? "))

# Create a turtle object
t = turtle.Turtle()

# Set the shape of the turtle (can be 'circle', 'arrow', 'square', 'turtle', etc.)
t.shape('turtle')

# Draw the square/rectangle
for _ in range(4):
    t.forward(size)  # Move the turtle forward by 'size' units
    t.right(90)      # Turn the turtle 90 degrees to the right

# Keep the window open until it is closed manually
turtle.mainloop()