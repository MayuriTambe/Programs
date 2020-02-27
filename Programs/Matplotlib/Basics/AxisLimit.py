
import matplotlib.pyplot as plt
X = range(1, 20)
Y = [value + 20 for value in X]

plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')

print(plt.axis()) 

plt.axis([0, 100, 0, 200]) 

plt.show()







