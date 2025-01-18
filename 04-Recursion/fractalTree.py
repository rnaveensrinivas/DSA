from turtle import Turtle, Screen

def tree(t: Turtle, 
         length: float = 150, 
         angle: float = 30, 
         decay: float = 25) -> None:
    """Recursively draws a fractal tree using turtle graphics with varying colors and branch widths.
    
    Parameters:
    - t (Turtle): The turtle object used to draw the tree.
    - length (float): The initial length of the tree's main branch. Defaults to 150.
    - angle (float, optional): The angle at which the turtle turns when drawing branches. 
    - decay (float, optional): The amount by which the length of each branch decreases in the recursive calls. 
    """

    if length > 0:
        t.forward(length) 
        
        # Draw right subtree
        t.right(angle)
        tree(t, length - decay, angle, decay)
        
        # Draw left subtree
        t.left(angle * 2)
        tree(t, length - decay, angle, decay)
        
        # Reset position, and orientation
        t.right(angle)
        t.backward(length)

if __name__ == "__main__":
    t = Turtle()
    t.speed("fastest")  # Use fastest for large drawings

    # Set initial position and orientation
    t.penup()
    t.setpos(0, -300)
    t.left(90)
    t.pendown()

    tree(t, length=150)

    # Keep the window open
    my_wnd = Screen()
    my_wnd.exitonclick()
