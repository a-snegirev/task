import random
import matplotlib.pyplot as plt
n = 10**3
def distance(x, y):
    return (x ** 2 + y ** 2) ** 0.5

dotsround = []
for i in range(0, n, 1):
    if distance((random.random() - 0.5) * 2, (random.random() - 0.5) * 2) <= 1:
        dotsround.append(1)
pi = 4*len(dotsround) / n

def pi_error(n,pi):
    return pi*(pi-1)/n**0.5

print('pi = ',pi,' +- ', pi_error(n,pi)*pi)

xs = [2**k for k in range(10,25)]
ys = [pi_error(x,pi) for x in xs]
plt.plot(xs,ys)
plt.scale('log')
plt.show
