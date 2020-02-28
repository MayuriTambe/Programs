import matplotlib.pyplot as plt
import numpy as np
weight1=[66,77,43,89,42]
height1=[112,114,117,77,89]
weight2=[65,87,92,54,88]
height2=[152,176,148,140,154]
weight3=[68,67,98,44,65]
height3=[165,167,156,197,154]
weight=np.concatenate((weight1,weight2,weight3))
height=np.concatenate((height1,height2,height3))
plt.scatter(weight, height, marker='*', color=['green','cyan','blue'])
plt.xlabel('weight', fontsize=16)
plt.ylabel('height', fontsize=16)
plt.title('Group wise Weight vs Height scatter plot',fontsize=20)
plt.show()