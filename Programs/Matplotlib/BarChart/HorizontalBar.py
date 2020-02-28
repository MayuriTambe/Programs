import matplotlib.pyplot as plt
import numpy as np

languges=["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
Popularity=[ 22.2, 17.6, 8.8, 8, 7.7, 6.7]

xposition=np.arange(len(languges))

plt.barh(xposition,Popularity,color='red')
plt.title("Popularity of programming Languages")
plt.yticks(xposition,languges)

plt.xlabel("Languges")
plt.ylabel('Popularity')

plt.grid(which="major",linestyle="-",linewidth="0.3",color="blue")
plt.grid(which="minor",linestyle="--",linewidth="0.5",color="green")
plt.minorticks_on()

plt.show()