import pandas as pd
import  numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from seaborn import set_style

Data=sns.load_dataset("iris")
sns.violinplot(x="sepal_length",y="species",data=Data)
sns.set_style("dark")
plt.show()