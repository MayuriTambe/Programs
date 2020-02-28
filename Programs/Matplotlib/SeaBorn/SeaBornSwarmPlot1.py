import pandas as pd
import  numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import style
from seaborn import set_style

Data=sns.load_dataset("tips")
set_style("dark")

sns.swarmplot(x="day",y="total_bill",data=Data)
sns.set_style("dark")
plt.show()