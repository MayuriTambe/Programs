import pandas as pd
import numpy as np

from pylab import randn
from matplotlib import pyplot as plt

X=randn(100)
Y=randn(100)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.scatter(X,Y, color="r")
plt.show()