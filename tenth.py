import math

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object with x and y coordinates.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a string representation of the Point object.
        """
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        """
        Calculate the Euclidean distance between self and another Point object.
        
        Args:
            other (Point): Another point to calculate the distance to.
        
        Returns:
            float: The distance between the two points.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# Example usage:
point1 = Point(3, 4)
point2 = Point(7, 1)

print("Point 1:", point1)
print("Point 2:", point2)

dist = point1.distance(point2)
print(f"Distance between {point1} and {point2}: {dist:.2f}")
