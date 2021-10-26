import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 50)

ax.set_xlim((-20, 20))
ax.set_ylim((-20, 20))
# Функция: y = (x + 2)^2 и y = (x + 2)^2 +- q
y1 = x**2
y2 = (x - 4)**2 - 5

plt.grid(True)
plt.legend(['y = x\u00B2', f'y = (x + 2)\u00B2'], loc=2)
plt.title('График функции y = (x + 2)\u00B2')
plt.savefig('img/grafic.png', dpi=500)
ax.plot(x, y1)
ax.plot(x, y2)
plt.show()