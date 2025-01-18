from turtle import Turtle, Screen
from random import randint

def get_color(length: float) -> str:
    """Returns a color based on the branch length."""
    if length > 70:
        return "brown"  # branches
    elif length > 40:
        return "dark green"  # middle branches
    else:
        return "green"  # leaves

def tree(t: Turtle, 
         length: float = 150, 
         width: float = 2,
         angle: float = None, 
         decay: float = None) -> None:
    """Recursively draws a fractal tree using turtle graphics with varying colors and branch widths.
    
    Parameters:
    - t (Turtle): The turtle object used to draw the tree.
    - length (float): The initial length of the tree's main branch. Defaults to 150.
    - width (float): The initial width of the tree's branches. Defaults to 2.
    - angle (float, optional): The angle at which the turtle turns when drawing branches. If not provided, a random angle between 20 and 50 degrees is used.
    - decay (float, optional): The amount by which the length of each branch decreases in the recursive calls. If not provided, a random decay value between 10 and 30 is used.

    The function uses recursion to draw smaller branches at each step, with the length and width of the branches decreasing progressively. The color of the branches also changes based on the branch length, transitioning from brown for thicker branches to green for thinner branches and leaves. 
    """

    if length > 0 and width > 0:
        
        # Set the width
        t.width(width)
        # Set the color based on the length
        t.pencolor(get_color(length))
        
        t.forward(length) 
        
        # use random values if not given
        use_angle = angle if angle else randint(20, 50)
        use_decay = decay if decay else randint(10, 30)
        
        # Draw right subtree
        t.right(use_angle)
        tree(t, length - use_decay, width - 1, angle, decay)
        
        # Draw left subtree
        t.left(use_angle * 2)
        tree(t, length - use_decay, width - 1, angle, decay)
        
        # Reset width, color, position, and orientation
        t.width(width)
        t.pencolor(get_color(length))
        t.right(use_angle)
        t.backward(length)

if __name__ == "__main__":
    t = Turtle()
    t.speed("fastest")  # Use fastest for large drawings

    # Set initial position and orientation
    t.penup()
    t.setpos(0, -300)
    t.left(90)
    t.pendown()

    # Draw the fractal tree with varying colors from brown to green
    tree(t, length=150, width=8)

    # Keep the window open
    my_wnd = Screen()
    my_wnd.exitonclick()
