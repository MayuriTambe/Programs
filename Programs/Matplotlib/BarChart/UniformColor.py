import matplotlib.pyplot as plt
import numpy as np

languges=["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
Popularity=[ 22.2, 17.6, 8.8, 8, 7.7, 6.7]

xposition=np.arange(len(languges))
plt.title("Popularity of programming Languages")
plt.bar(xposition,Popularity,color=(0.2,0.4,0.6,0.6))

plt.xticks(xposition,languges)
plt.xlabel("languges")
plt.ylabel('Popularity')

plt.grid(True,color="k")
plt.minorticks_on()
plt.grid(which="major",linestyle="-",linewidth="0.3",color="blue")
plt.grid(which="minor",linestyle="--",linewidth="0.5",color="green")
plt.show()
