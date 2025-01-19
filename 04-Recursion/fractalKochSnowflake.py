from turtle import Turtle, Screen
from Point import Point    
from fractalMountain import mountain

def koch_snowflake(t: Turtle, 
                   p1: Point, p2: Point, p3: Point,
                   threshold: int = 5) -> None:
    """
    Draw a Koch snowflake fractal using the fractal mountain algorithm.

    The Koch snowflake is a fractal curve that starts with an equilateral triangle. 
    At each recursive step, the line segments of the triangle are divided and a triangular 
    "bump" is added to form increasingly intricate shapes. This implementation uses 
    the `mountain` function to recursively generate the fractal.

    Parameters:
    t (Turtle): The Turtle object used for drawing.
    p1 (Point): The first vertex of the equilateral triangle.
    p2 (Point): The second vertex of the equilateral triangle.
    p3 (Point): The third vertex of the equilateral triangle.
    threshold (int, optional): The minimum distance between points at which recursion stops. 
                               Lower values result in more detailed fractals. Default is 5.

    Notes:
    - This function leverages the `mountain` function to recursively draw the edges 
      of the snowflake. Each edge is divided into smaller segments, and the middle 
      segment is replaced with a triangular peak.
    - The recursion ends when the distance between points falls below the `threshold`.
    - To create a complete snowflake, this function draws the fractal for each side 
      of the initial triangle (p1->p2, p2->p3, p3->p1).
    - Ensure that the points `p1`, `p2`, and `p3` form an equilateral triangle for 
      accurate results.

    Example:
    >>> from turtle import Turtle
    >>> t = Turtle()
    >>> t.speed("fastest")
    >>> p1 = Point(-200, 100)
    >>> p2 = Point(200, 100)
    >>> p3 = Point(0, -200)
    >>> koch_snowflake(t, p1, p2, p3, threshold=5)
    >>> t.getscreen().exitonclick()
    """
    mountain(t, p1, p3, threshold)
    mountain(t, p3, p2, threshold)
    mountain(t, p2, p1, threshold)

        
if __name__ == "__main__": 
    t = Turtle()
    t.speed("fastest")
    
    p1 = Point(-150,0)
    p2 = Point(150,0)
    p3 = Point(0,300)

    koch_snowflake(t, p1, p2, p3, 10)
    
    my_wnd = Screen()
    my_wnd.exitonclick()
    