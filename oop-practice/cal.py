import numpy as np
import matplotlib.pyplot as plt

class Calculus:
    def __init__(self, start=-2*np.pi, end=2*np.pi, num_points=100):
        self.start = start
        self.end = end
        self.num_points = num_points

    def numerical_derivative(self, function, x):
        h = 1e-6  # used for small numerical differentiation
        return (function(x + h) - function(x)) / h

    def numerical_integral(self, function, a, b):
        x_values = np.linspace(a, b, self.num_points)
        y_values = function(x_values)
        dx = (b - a) / self.num_points
        return np.sum(y_values) * dx

    def mean_value_theorem(self, function, a, b):
        # average rate of change
        avg_rate_of_change = (function(b) - function(a)) / (b - a)

        # finds a point c where the derivative equals the average rate of change
        c = (a + b) / 2
        derivative_at_c = self.numerical_derivative(function, c)

        return c, avg_rate_of_change, derivative_at_c

if __name__ == "__main__":
    calc_instance = Calculus()

    # this plots the sin function
    x_sine = np.linspace(calc_instance.start, calc_instance.end, calc_instance.num_points)
    y_sine = np.sin(x_sine)
    plt.plot(x_sine, y_sine, label='sin(x)')

    # [0, pi]
    a = 0
    b = np.pi
    c, avg_rate, derivative_at_c = calc_instance.mean_value_theorem(np.sin, a, b)

    # plots the interval [a, b]
    plt.axvspan(a, b, color='gray', alpha=0.2, label='Interval [0 to pi]')

    # plots the point c
    plt.scatter(c, np.sin(c), color='red', label='Point c')

    # build out the plot
    plt.title('Mean Value Theorem for sine function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Interval [0 to pi]: Average Rate of Change = {avg_rate}")
    print(f"Point c: Derivative at c = {derivative_at_c}")
