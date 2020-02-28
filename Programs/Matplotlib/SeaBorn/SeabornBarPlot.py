import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns

Data=sns.load_dataset("titanic")
plt.title("Survival in titanic")
sns.barplot(x="sex",y="survived",hue="embark_town",data=Data)
plt.show()