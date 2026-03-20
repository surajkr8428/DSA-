import numpy as np
import matplotlib.pyplot as plt

# Constant value
y_value = np.pi ** 4

# x range
x = np.linspace(-10, 10, 400)
y = np.full_like(x, y_value)

# Plot
plt.plot(x, y, label=r"$y = \pi^4$")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of y = π⁴")
plt.legend()
plt.grid(True)
plt.show()
