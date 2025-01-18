from turtle import Turtle, Screen
import math
from typing import Tuple

class Point:
    """Represents a point in 2-D Euclidean Space."""

    def __init__(self, x: float, y: float) -> None:
        """Initialize a point with x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Return a string representation of the point."""
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """Return a formal string representation of the point."""
        return f"Point({self.x}, {self.y})"
    
    def midpoint(self, another_point: 'Point') -> 'Point':
        """Calculate and return the midpoint between this point and another point."""
        mid_x = (self.x + another_point.x) / 2
        mid_y = (self.y + another_point.y) / 2
        return Point(mid_x, mid_y)

    def distance_to(self, another_point: 'Point') -> float:
        """Return the Euclidean distance between this point and another point."""
        return math.sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)

    def get_values(self) -> Tuple[float, float]:
        """Return the coordinate values as tuple."""
        return (self.x, self.y)
    
    
COLORMAP = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    
def sierpinski_triangle(t: Turtle, 
                        p1: Point, 
                        p2: Point,
                        p3: Point, 
                        degree: int = 5) -> None: 
    """Given three points draw a Sierpinski Triangle recursively."""
    
    if p1.distance_to(p2) > 5 and 0 <= degree <= 6: 
        # Base case: edge of triangle should be greater than 5.
        
        # Go to starting position
        t.penup()
        t.setpos(p1.get_values())
        t.pendown()
        
        t.fillcolor(COLORMAP[degree])
        t.begin_fill()
        # Draw the triangle
        t.setpos(p2.get_values())
        t.setpos(p3.get_values())
        t.setpos(p1.get_values())
        t.end_fill()
        
        # Get the midpoints
        mid_p1_p2 = p1.midpoint(p2)
        mid_p1_p3 = p1.midpoint(p3)
        mid_p2_p3 = p2.midpoint(p3)
        
        # Recursively draw the smaller triangles
        sierpinski_triangle(t, p1, mid_p1_p2, mid_p1_p3, degree-1)
        sierpinski_triangle(t, mid_p1_p2, p2, mid_p2_p3, degree-1)
        sierpinski_triangle(t, mid_p1_p3, mid_p2_p3, p3, degree-1)
        

if __name__ == "__main__": 
    t = Turtle()
    
    p1 = Point(-150, 0)
    p2 = Point(0, 300)
    p3 = Point(150, 0)
    sierpinski_triangle(t, p1, p2, p3, degree=3)
    
    my_wnd = Screen()
    my_wnd.exitonclick()