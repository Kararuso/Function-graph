import matplotlib.pyplot as plt
import numpy as np
import random

fig, ax = plt.subplots()
ax.set_xlim((-500, 500))
ax.set_ylim((-500, 500))
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.savefig('grafic.png', dpi=400)
plt.grid(True)
plt.title("Cдвиг квадратичной функции", size=20)
x = np.linspace(-5, 5, 100)
a = random.randint(1, 100)
b = random.randint(1, 100)
print(a)
print(b)
y = int(a) * x + int(b)

#Примеры формул
# y = ((int(a)) * (x**2)) + (int(b))
# y = x**2 - парабола
# y = x**2 + 1
# y = x**0.5 или y = sqrt(x)
# y = 1 / x
# y = (x + 3)**2
# y = (x**2 - 1) / x
# y = (4 * x) / (4 + x**2)
# y = 1/4 * x**2 - 5
# -------------
# Функция y = kx + l
# k = int(input("k = "))
# l = int(input("l = "))
# k = random.randint(-10,50)
# b = random.randint(-10,50)
# y = k * x + b
# -------------2
ax.plot(x, y)

plt.show()


