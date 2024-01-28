class Circle:
    def __init__(self, radius):
        self._radius = radius
        
    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __str__(self):
        return f"Circle with radius: {self.radius}"
    
    @property # getter method for radius
    def radius(self):
        return self._radius
    
    
    @property
    def diameter(self):
        return self._radius * 2
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = value 
    
if __name__ =="__main__":
    
    circle1 = Circle(5)
    
    print(circle1)
    # prints Circle with radius, 5, without the repr and str methods, it would print object code like this: 
    # <__main__.Circle object at 0x0000016928D36908>
    # now, if I remove/comment out __str__ method and run the script, python will default to the __repr__ method and output will be as follows:
    # Circle(radius=5)
    
    # I considered creating a setter for diameter, but I don't think it would be good practice to create a setter for attributes that are dependent 
    # upon other attributes. So, setters here should only be used for independent attributes, like radius!