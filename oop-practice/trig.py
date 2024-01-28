import numpy as np
import matplotlib.pyplot as plt

class Trig:
    def __init__(self, start=-2*np.pi, end=2*np.pi, num_points=100):
        self.start = start
        self.end = end
        self.num_points = num_points

    def trig_function(self, function_name='sin'):
        x = np.linspace(self.start, self.end, self.num_points)

        if function_name == 'sin':
            y = np.sin(x)
            title = 'Sine Function'
        elif function_name == 'cos':
            y = np.cos(x)
            title = 'Cosine Function'
        elif function_name == 'tan':
            y = np.tan(x)
            title = 'Tangent Function'
        else:
            raise ValueError("Invalid function_name. Use 'sin', 'cos', or 'tan'.")

        plt.plot(x, y)
        plt.title(title)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    obj = Trig()
    obj.trig_function('sin')
    obj.trig_function('cos')
    obj.trig_function('tan')
