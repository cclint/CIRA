class Adder:
    def __init__(self, value=0): # sets the value class variable and sets the value to 0
        self.value = value

    def __repr__(self): 
        return f"Adder(value={self.value})" # gives a string representation of the object that is meant for debugging. When this is called, it returns a string that would create an object with the same state. this would return the value of adder

    def __str__(self):
        return f"Current value: {self.value}" # this returns a human readable string representation as the object. So, if you print(object), it will return the value of the Adder object. 

    def add(self, num): # this method actually does the adding 
        self.value += num
        return self.value

# Example usage
if __name__ == "__main__":
    my_adder = Adder()

    print("Initial state:")
    print(my_adder)  # calls __str__

    print("\nAdding 5:")
    my_adder.add(5)
    print(my_adder) # output should be 5

    print("\nAdding 10:")
    my_adder.add(10) # output should be 15
    print(my_adder)

    print("\nRepresentation of the Adder object:")
    print(repr(my_adder))  # calls __repr__


