
import matplotlib.pyplot as plt
import numpy as np

languges=["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
Popularity=[ 22.2, 16, 8.8, 8, 7.7, 6.7]

xposition=np.arange(len(languges))


yposition=[0,4,1,5,8,9]

plt.xticks(yposition,languges,color="green")
plt.ylabel("Popularity")
plt.xlabel("languges")
plt.title("Popularity of programming Languages")

plt.grid(which="major",linestyle="--",linewidth=0.2,color="red")
plt.minorticks_on()
plt.grid(which="minor",linestyle="--",linewidth=0.2,color="black")

plt.bar(yposition,Popularity,color="pink")
plt.show()