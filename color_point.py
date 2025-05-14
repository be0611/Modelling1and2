from point import Point
import random

class PointException(Exception):
    """
    Custom exception class for handling point-related errors.
    Currently unused, but can be extended for specific Point errors.
    """
    pass

class ColorPoint(Point):
    """
    Represents a colored point on a 2D plane.
    Inherits from the Point class and adds a color attribute.
    """

    def __init__(self, x, y, color):
        """
        Initializes a ColorPoint with x, y coordinates and a color.

        :param x: Numeric value for the x-coordinate
        :param y: Numeric value for the y-coordinate
        :param color: A string representing the color of the point
        :raises TypeError: If x or y are not numeric
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")

        super().__init__(x, y)  # Call the parent Point class initializer
        self.color = color

    def __str__(self):
        """
        Returns a string representation of the ColorPoint.

        :return: A string in the format <color: x, y>
        """
        return f"<{self.color}: {self.x}, {self.y}>"


if __name__ == "__main__":
    # Create and display a single ColorPoint
    p = ColorPoint(1, 2, "red")
    print(p.distance_orig())  # Should return the distance from origin
    print(p)                  # Should print: <red: 1, 2>

    # Uncomment the following block to test random ColorPoints and sorting
    """
    colors = ["red", "green", "blue", "yellow", "black", "magenta",
              "cyan", "white", "burgundy", "periwinkle", "marsala"]

    color_points = []
    for i in range(10):
        color_points.append(
            ColorPoint(
                random.randint(-10, 10),     # x-coordinate
                random.randint(-10, 10),     # y-coordinate
                random.choice(colors)        # random color
            )
        )

    print("Generated color points:")
    print(color_points)

    color_points.sort()  # Sorts based on distance from origin (uses Point's __gt__)
    print("Sorted color points by distance from origin:")
    print(color_points)
    """
