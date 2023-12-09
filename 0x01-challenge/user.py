#!/usr/bin/python3
""" 
User class la land
"""

class User():
    """ Documentation more than one word """

    def __init__(self):
        """ Documentation more than one word """
        self.__email = None

    @property
    def email(self):
        """ Documentation more than one word """
        return self.__email

    @email.setter
    def email(self, value):
        """ Documentation more than one word """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    """ init of app """
    u = User()
    u.email = "john@snow.com"
    print(u.email)
