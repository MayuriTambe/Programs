import pandas as pd
import  numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import style
from seaborn import set_style

Data=sns.load_dataset("tips")
sns.scatterplot(x="day",y="total_bill",hue="time",data=Data)
set_style("darkgrid")
plt.show()