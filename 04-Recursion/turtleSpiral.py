from turtle import Turtle, Screen

def draw_spiral(t: Turtle, 
                length: float, 
                angle: float, 
                decay: float = 0.01) -> None:
    """Draw a spiral using turtle."""
    if length > 0: 
        t.forward(length)
        t.right(angle)
        draw_spiral(t, length - decay, angle, decay)

if __name__ == "__main__":
    t = Turtle()
    t.speed("fastest")  # Speed up drawing
    
    # Optional: Starting position
    t.penup()
    t.setpos(0, 200)  # Move to (0, 200) , (x, y)
    t.pendown()
    
    # Draw the spiral
    draw_spiral(t, length=7, angle=5, decay=0.01)
    
    # Keep the window open
    my_win = Screen()
    my_win.exitonclick()
