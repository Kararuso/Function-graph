import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim((-15, 15))
ax.set_ylim((-15, 15))
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.savefig('img/grafic.png', dpi=400)
plt.grid(True)
plt.title("Cдвиг квадратичной функции", size=20)
x = np.linspace(-5, 5, 100)
a = input("Введите а = ")
q = input("Введите q = ")
y1 = (float(a)) * (x**2)
y2 = (float(a)) * (x**2) + (float(q))
if float(q) > 0:
    plt.legend([f' y = ax\u00B2 + {q}', ' y = ax\u00B2'], loc=2)
else:
    plt.legend([' y = ax\u00B2', f' y = ax\u00B2 {q}'], loc=2)
ax.plot(x, y1)
ax.plot(x, y2)
plt.show()

