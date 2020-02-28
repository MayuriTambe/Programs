import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

languages=["Java","Python", "PHP", "JavaScript","C#", "C++"]
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

explode=[0.1,0,0,0,0,0]

plt.pie(Popularity,labels=languages,explode=explode,shadow=True)
plt.title("Popularity of programming Languages")
plt.show()
