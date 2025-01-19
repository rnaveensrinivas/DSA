from turtle import Turtle, Screen
from Point import Point    

def mountain(t: Turtle, p1: Point, p2: Point, threshold: int = 5) -> None:
    """
    Recursively draw a fractal mountain between two points, p1 and p2.

    This function divides the line segment between p1 and p2 into smaller segments, 
    and at each step, calculates the perpendicular height to form a triangle. 
    The process continues recursively, creating smaller and smaller triangles 
    to form a fractal mountain shape.

    The base case is when the distance between p1 and p2 is smaller than a threshold, 
    at which point the function stops and draws a line directly between the two points.

    The mountain shape follows this structure:

             p4
             /\
            /  \
           /    \
     ------      ------
    p1    p3    p5    p2

    Parameters:
    t (Turtle): The Turtle object used to draw the fractal.
    p1 (Point): The starting point of the line segment.
    p2 (Point): The ending point of the line segment.
    threshold (int): The minimum distance between points at which the recursion stops. 
                     If the distance between p1 and p2 becomes smaller than this value, 
                     the function draws a straight line between the points and terminates.
    
    Notes:
    - The function recursively divides the segment into three parts and calculates 
      a perpendicular point at each step.
    - The perpendicular point is calculated using the `perpendicular_point` method, 
      with a factor of 3, to control the height of the peaks.
    - The recursion terminates when the distance between p1 and p2 becomes smaller than 5.
    """
    if p1.distance_to(p2) < threshold:
        t.penup()
        t.setpos(p1.get_values())
        t.pendown()
        t.setpos(p2.get_values())
    else: 
        p3 = Point(p1.x + (p2.x - p1.x) / 3, p1.y + (p2.y - p1.y) / 3)
        p4 = p1.perpendicular_point(p2, factor=2)
        p5 = Point(p2.x - (p2.x - p1.x) / 3, p2.y - (p2.y - p1.y) / 3)
         
        mountain(t, p1, p3)
        mountain(t, p3, p4)
        mountain(t, p4, p5)
        mountain(t, p5, p2)

        
if __name__ == "__main__": 
    t = Turtle()
    t.speed("fastest")
    
    p1 = Point(-300,0)
    p2 = Point(300,0)
    
    mountain(t, p1, p2)
    
    my_wnd = Screen()
    my_wnd.exitonclick()
    