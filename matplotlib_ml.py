import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 20)
y = x ** 3
print(x)
print(y)
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('X cube')
plt.title('X VS X cube')
plt.show()

## subplotting

plt.subplot(1, 3, 1)  # subplot 1
plt.plot(x, x, 'r')
plt.xlabel('X')
plt.ylabel('X ')
plt.title('X VS X ')

plt.subplot(1, 3, 2)  # subplot 2
plt.plot(x, x ** 2, 'g')
plt.xlabel('X')
plt.ylabel('X square')
plt.title('X VS X square')

plt.subplot(1, 3, 3)  # subplot 3
plt.plot(x, x % 2, 'b')
plt.xlabel('X')
plt.ylabel('X mod 2')
plt.title('X VS X mod 2')

plt.tight_layout()
plt.show()

## 2ND METHOD TO PLOT

p1 = plt.figure()
a = p1.add_axes([.1, .1, .9, .9])
a.plot(x, y)
plt.xlabel('X')
plt.ylabel('X cube')
plt.title('X VS X cube')
plt.show()

p1 = plt.figure()
a = p1.add_axes([0.1, 0.1, .8, .8])
a.plot(x, x % 8, 'g')
plt.xlabel('X')
plt.ylabel('X mod 5')
plt.title('X VS X mod 5')

b = p1.add_axes([.2, .6, .2, .2])
b.plot(x, np.log(x))
plt.xlabel('X')
plt.ylabel('log(X)')
plt.title('X VS log(X)')
plt.tight_layout()
plt.show()

## subplotting

p2, c = plt.subplots(nrows=1, ncols=3)
c[0].plot(x, x, 'r')
c[0].set_xlabel('X')
c[0].set_ylabel('X ')
c[0].set_title('X VS X ')

c[1].plot(x, x ** 2, 'g')
c[1].set_xlabel('X')
c[1].set_ylabel('X square')
c[1].set_title('X VS X square')

c[2].plot(x, x % 2, 'b')
c[2].set_xlabel('X')
c[2].set_ylabel('X mod 2')
c[2].set_title('X VS X mod 2')
plt.tight_layout()
plt.show()

p = plt.figure()
a = p.add_axes([.1, .1, .8, .8])
a.plot(x, x % 4, label='mod 4')
a.plot(x, np.log(x), label='log(x)')
a.legend()
plt.show()
