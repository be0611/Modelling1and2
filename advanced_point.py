from color_point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    """
    Represents a more advanced colored point with coordinate validation,
    color checking, and enhanced utility methods like custom constructors and distance calculations.
    """

    COLORS = ["red", "green", "blue", "yellow", "black", "periwinkle", "white"]

    def __init__(self, x, y, color):
        """
        Initializes an AdvancedPoint with x, y coordinates and a color.

        :param x: Numeric x-coordinate
        :param y: Numeric y-coordinate
        :param color: A string representing the color
        :raises PointException: If color is not in the allowed COLORS list
        """
        if color not in self.COLORS:
            raise PointException(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Getter for the x-coordinate.
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate.
        """
        self._x = value

    @property
    def y(self):
        """
        Getter for the y-coordinate.
        """
        return self._y

    @property
    def color(self):
        """
        Getter for the color of the point.
        """
        return self._color

    @classmethod
    def add_color(cls, color):
        """
        Adds a new valid color to the class-level COLORS list.

        :param color: A string representing the new color to allow
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Creates an AdvancedPoint from a tuple of coordinates.

        :param coordinate: A tuple of two values (x, y)
        :param color: Optional color (defaults to "red")
        :return: An AdvancedPoint instance
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculates the distance between two AdvancedPoint instances.

        :param p1: First AdvancedPoint
        :param p2: Second AdvancedPoint
        :return: Euclidean distance between p1 and p2
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Calculates the distance from this point to another AdvancedPoint.

        :param p: Another AdvancedPoint
        :return: Euclidean distance between self and p
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5


# Example usage
AdvancedPoint.add_color("rojo")              # Add a new color to allowed list
p = AdvancedPoint(1, 2, "rojo")              # Create a point with new color
print(p.x)                                   # Access x-coordinate
print(p)                                     # Will use inherited __str__ from ColorPoint
print(p.distance_orig())                     # Inherited from Point class

p2 = AdvancedPoint.from_tuple((3, 2))        # Create a point from tuple with default color
print(p2)

print(AdvancedPoint.distance_2_points(p, p2))  # Static method to measure distance between p and p2
