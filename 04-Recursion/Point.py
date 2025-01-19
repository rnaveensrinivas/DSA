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
    
    def __add__(self, another_point: 'Point') -> 'Point':
        """Add two points together (coordinate-wise)."""
        if not isinstance(another_point, Point):
            return ValueError("Argument is not a type of 'Point'!")
        return Point(self.x + another_point.x, self.y + another_point.y)
    
    def __sub__(self, another_point: 'Point') -> 'Point':
        """Add two points together (coordinate-wise)."""
        if not isinstance(another_point, Point):
            return ValueError("Argument is not a type of 'Point'!")
        return Point(self.x - another_point.x, self.y - another_point.y)
    
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
    
    def perpendicular_point(self, another_point: 'Point', factor: int = 3) -> 'Point':
        """
        Find a point perpendicular to the line segment between 'this' point and 'another_point',
        starting from the their midpoint, at a distance of (line segment length / factor).

        The function calculates the perpendicular direction to the line segment between `this` 
        point and `another_point`, then moves from the midpoint by a distance of (line segment length / factor).

        The resulting point is the desired perpendicular point.

                p4
                /\
               /  \
              /    \
        ------      ------
        p1   p3    p5    p2
        
        In the diagram:
        - p1 and p2 are the input points defining the line segment.
        - p3 is the midpoint between p1 and p2.
        - p4 is the perpendicular point calculated by this function.
        - p4 is at a distance of len([p1,p3])/(factor=3)
        
        A factor of 1 is just a equvialateral triangle. 
        
                p4
                /\
               /  \
              ------
              p1  p2        

        Args:
            another_point (Point): The second point defining the line segment.
            factor (int, optional): The factor by which the segment length is divided. Default is 3.
        
        Returns:
            Point: The perpendicular point at the desired distance from the midpoint.
        """

        # Step 1: Find the midpoint
        mid = self.midpoint(another_point)
        
        # Step 2: Calculate direction vector
        dx = another_point.x - self.x
        dy = another_point.y - self.y
        
        # Step 3: Find a perpendicular vector (swap and negate one component)
        px = -dy
        py = dx
        
        # Step 4: Calculate the length of the direction vector
        length = self.distance_to(another_point) / factor
        
        # Step 5: Normalize the perpendicular vector to the desired distance
        scale = (math.sqrt(3) / 2) * length / math.sqrt(px ** 2 + py ** 2)
        
        # Step 6: Scale and return the new point
        new_x = mid.x + scale * px
        new_y = mid.y + scale * py
        
        return Point(new_x, new_y)