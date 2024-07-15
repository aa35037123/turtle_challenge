import numpy as np
import matplotlib.pyplot as plt

def piecewise_function(x, k=0.24):
    # Apply the sigmoid function for x > 80
    sigmoid_part = 100 / (1 + np.exp(-k * (x - 78)))
    # Apply the linear function for x <= 80
    slope = (100 / (1 + np.exp(-k * (80 - 78)))) / 80
    linear_part = slope * x
    
    # Combine the two parts using numpy's where function
    return np.where(x > 80, sigmoid_part, linear_part)

x_values = np.linspace(0, 100, 400)
y_values = piecewise_function(x_values)

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sigmoid Function')
plt.grid(True)
plt.show()