import turtle

# Recursive function to draw the tree
def drawTree(branch, t):
    if branch > 5:
        t.forward(branch)        # Move forward by the length of the branch
        t.right(20)              # Turn right by 20 degrees

        drawTree(branch - 15, t) # Recursively draw the right subtree

        t.left(40)               # Turn left by 40 degrees
        drawTree(branch - 15, t) # Recursively draw the left subtree

        t.right(20)              # Turn right by 20 degrees to return to the initial direction
        t.backward(branch)       # Move back to the previous branch

# Main function to set up the turtle environment and draw the tree
def main():
    t = turtle.Turtle()          # Create a turtle object
    window = turtle.Screen()     # Set up the screen/window

    t.left(90)                   # Point the turtle upwards (90 degrees)
    t.up()                       # Lift the pen up (so no drawing while moving)
    t.backward(200)              # Move the turtle back by 200 units
    t.down()                     # Put the pen down (to start drawing)
    t.color("green")             # Set the color to green

    drawTree(100, t)             # Call the recursive function to draw the tree

    window.exitonclick()          # Close the window when clicked

# Call the main function to execute the program
main()