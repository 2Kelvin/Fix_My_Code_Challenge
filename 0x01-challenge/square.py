#!/usr/bin/python3
""" Class Square module """


class Square():
    """Class Square to create squares."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Init Square method to create square instances."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        if not hasattr(self, "height"):
            self.height = self.width

    def area_of_my_square(self):
        """Area of the square."""
        return self.width * self.width

    def perimeterOfMySquare(self):
        """Calculates the perimeter of a square."""
        return (self.width * 4)

    def __str__(self):
        """Custom string object."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Code should not run when imported."""
    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeterOfMySquare())
