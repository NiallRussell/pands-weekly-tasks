import matplotlib.pyplot as plt
import random
mu = 5
sigma = 2
data = []
for i in range (1000):
    value = random.gauss(mu, sigma)
    data.append(value)

plt.hist(data)
plt.show()