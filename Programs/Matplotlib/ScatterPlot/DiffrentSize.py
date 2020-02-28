import  numpy as np
import matplotlib.pyplot as plt

x1 = np.random.randn(20)
x2 = np.random.randn(20)
x3=np.random.randn(20)
plt.figure(1)

plt.plot(x1, 'bo', markersize=20)
plt.plot(x2, 'ro', markersize=15)
plt.plot(x3, "go" ,markersize=10)
plt.show()