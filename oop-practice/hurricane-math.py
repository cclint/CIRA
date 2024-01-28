import numpy as np
import matplotlib.pyplot as plt

class HurricaneModel:
    def __init__(self, initial_position):
        self.position = np.array(initial_position, dtype=float)

    def curl_vector_field(self, x, y):
        # 2D vector field representing hurricane swirls
        u = -y
        v = x
        return u, v

    def update_position(self, dt):
        x, y = self.position
        u, v = self.curl_vector_field(x, y)

        # update the position based on the vector field
        self.position[0] += u * dt
        self.position[1] += v * dt

    def plot_hurricane_path(self, num_steps=200, dt=0.1):
        path = []

        for _ in range(num_steps):
            path.append(self.position.copy())
            self.update_position(dt)

        path = np.array(path)
        plt.plot(path[:, 0], path[:, 1], label='Hurricane Path')
        plt.scatter(path[:, 0], path[:, 1], c=range(num_steps), cmap='viridis', label='Time')
        plt.colorbar(label='Time Step')
        plt.title('Hurricane Path Simulation')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    initial_position = [1.0, 0.0]  # Initial position as floating-point numbers
    
    hurricane = HurricaneModel(initial_position)
    hurricane.plot_hurricane_path(num_steps=200, dt=0.1)
