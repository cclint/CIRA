class Arithmetic:
    def __init__(self, a: int, b: int):
        """
        Initialize an instance of the Arithmetic class.

        Args:
        - a (int): First operand.
        - b (int): Second operand.
        """
        self.__a = a
        self.__b = b

    @property
    def a(self):
        """
        Getter method for the 'a' attribute.

        Returns:
        - int: The value of the 'a' attribute.
        """
        return self.__a

    @property
    def b(self):
        """
        Getter method for the 'b' attribute.

        Returns:
        - int: The value of the 'b' attribute.
        """
        return self.__b

    def __repr__(self):
        """
        Return a string representation of the Arithmetic object.

        Returns:
        - str: String representation.
        """
        return f"Arithmetic(a={self.a}, b={self.b})"

    def __str__(self):
        """
        Return a human-readable string representation of the Arithmetic object.

        Returns:
        - str: Human-readable string representation.
        """
        return f"Arithmetic(a={self.a}, b={self.b})"

    def adder(self):
        """
        Calculate the sum of 'a' and 'b'.

        Returns:
        - int: The result of adding 'a' and 'b'.
        """
        return self.a + self.b


if __name__ == "__main__":
    add_instance = Arithmetic(4, 4)
    print(add_instance.adder())  # accessing the result of addition

    # another instance with different values:
    zero_instance = Arithmetic(0, 0)
    print(zero_instance)  # accessing the string representation of the instance
