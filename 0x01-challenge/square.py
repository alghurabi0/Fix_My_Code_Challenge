#!/usr/bin/python3
""" documentation is nice """


class Square():
    """ My square that is very dumb """    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """ Initialization of the square inst """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ str method in classes """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ Init of app """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
