import matplotlib.pyplot as plt
import numpy as np

languges=["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
Popularity=[22.2, 17.6, 8.8, 8, 7.7, 6.7]

xposition=np.arange(len(languges))

plt.xticks(xposition,languges,color="green")
plt.ylabel("Popularity")
plt.xlabel("languges")
plt.title("Popularity of programming Languages")

plt.grid(which="major",linestyle="--",linewidth=0.5,color="red")
plt.minorticks_on()
plt.grid(which="minor",linestyle="--",linewidth=0.5,color="black")
plt.subplots_adjust(bottom=0.5, top=0.8)

plt.bar(xposition,Popularity)
plt.show()