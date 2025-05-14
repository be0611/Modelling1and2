import random

class Point:
    def __init__(self, x, y):
        """
        Initializes a Point object with x and y coordinates.

        :param x: The x-coordinate of the point
        :param y: The y-coordinate of the point
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a human-readable string representation of the point.

        :return: A string in the format <x, y>
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        """
        Returns an official string representation of the point.
        Uses the same format as __str__.

        :return: A string in the format <x, y>
        """
        return self.__str__()

    def distance_orig(self):
        """
        Calculates the distance from this point to the origin (0, 0)
        using the Euclidean distance formula.

        :return: A float representing the distance to the origin
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        Compares this point to another based on distance from the origin.

        :param other: Another Point object
        :return: True if this point is farther from the origin than the other, False otherwise
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        """
        Checks if this point is at the same distance from the origin as another point.

        :param other: Another Point object
        :return: True if both points are equidistant from the origin, False otherwise
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance


if __name__ == "__main__":
    # Instantiate a point at (1, 2)
    p = Point(1, 2)
    print(f"p.x = {p.x} and p.y = {p.y}")

    # Modify the x coordinate of the point
    p.x = 20
    print(f"p.x = {p.x} and p.y = {p.y}")

    # Display the point using __str__
    print(p)

    # Create a list of 5 random points with x and y in range [-10, 10]
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10, 10), random.randint(-10, 10)))

    print("I got these 5 random points: ")
    print(points)

    # Create a specific point and compute its distance from origin
    p = Point(3, 4)
    print(p.distance_orig())  # Expected output: 5.0 (3-4-5 triangle)

    # Compare distances of two points
    p2 = Point(1, 1)
    print(f"I am comparing p and p2: {p > p2}")  # Expected: True

    # Sort the list of points by distance from the origin
    print("The sorted list of points is: ")
    points.sort()
    print(points)
