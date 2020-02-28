import pandas as pd
import  numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import style
from seaborn import set_style

Data=sns.load_dataset("titanic")
set_style("dark")

sns.pointplot(x="sex",y="survived",hue="class",data=Data)
plt.show()