import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 500)

x_safe = x[x != 0]

y = 10 * np.cos(x_safe**2) / (x_safe**2)

plt.plot(x_safe, y, label='10*cos(x^2)/x^2', linewidth=2)

plt.title('Графік функції Y(x)', fontsize=15)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y(x)', fontsize=12, color='blue')

plt.legend()
plt.grid(True)

plt.show()
