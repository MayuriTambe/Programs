import pandas as pd
import numpy as np

from pylab import randn
from matplotlib import pyplot as plt


import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()

X=randn(1000)
Y=randn(1000)
figure=px.scatter(X,Y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
figure.show()
