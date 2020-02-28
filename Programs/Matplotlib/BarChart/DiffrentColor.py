import matplotlib.pyplot as plt
import numpy as np

languges=["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
Popularity=[ 22.2, 17.6, 8.8, 8, 7.7, 6.7]

xposition=np.arange(len(languges))
plt.title("Popularity of programming Languages")
plt.bar(xposition,Popularity,color=("red","blue","yellow","black","pink"))

plt.xticks(xposition,languges)
plt.xlabel("languges")
plt.ylabel('Popularity')


plt.minorticks_on()
plt.grid(which="major",linestyle="-",linewidth="0.3",color="black")
plt.grid(which="minor",linestyle="--",linewidth="0.5",color="green")
plt.show()