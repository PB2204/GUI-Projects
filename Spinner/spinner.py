from turtle import *

# Set up initial state
state = {'turn': 0}

# Create spinner function
def spinner():
    clear()
    angle = state['turn'] / 10
    
    # Draw three dots with different colors
    colors = ['red', 'green', 'blue']
    for color in colors:
        right(angle)
        forward(100)
        dot(120, color)
        back(100)
        right(120)
    
    update()

# Animate the spinner
def animate():
    if state['turn'] > 0:
        state['turn'] -= 1
    spinner()
    ontimer(animate, 20)

# Function to increase the spinner's turn
def flick():
    state['turn'] += 10

# Set up turtle screen
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)

# Bind the flick function to the space key
onkey(flick, 'space')
listen()

# Start the animation
animate()
done()