import pandas as pd
import numpy as np

from pylab import randn
from matplotlib import pyplot as plt
import plotly.express as px

X=randn(1000)
Y=randn(1000)
figure=px.scatter(X,Y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
figure.show()
