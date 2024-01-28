class Maths:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __repr__(self):
        return f"Maths(a={self.a}, b={self.b})"
    
    def __str__(self):
        return f"Maths(a={self.a}, b={self.b})"
    
    def adder(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def product(self):
        return self.a * self.b
    
    def divide(self):
        # uses integer division 
        return self.a // self.b

if __name__ == "__main__":
    obj = Maths(4, 4)
    print(obj.__str__())
    
    add = Maths(4, 4)
    print(add.adder())
    
    sub = Maths(4, 4)
    print(sub.subtract())
    
    multi = Maths(4, 4)
    print(multi.product())
    
    div = Maths(4, 4)
    print(div.divide())
