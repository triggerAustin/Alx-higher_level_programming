#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
        prints the first and last name

        Args:
            @first_name: string of the first name
            @last_name: string of the last name, defaulted to an empty string

        Raises:
            TypeError: names have to be strings
        
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
