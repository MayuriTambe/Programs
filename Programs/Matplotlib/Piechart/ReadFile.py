import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

dataframe=pd.read_csv("/home/admin1/Desktop/medal.csv")

gold_medal=dataframe["gold_medal"]
country=dataframe["country"]
plt.pie(gold_medal,labels=country,startangle=140,shadow=True)
plt.show()