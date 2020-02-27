
from matplotlib import pyplot as plt
from matplotlib import style

x=[5,8,10]
y=[12,16,6]
x1=[6,9,11]
y1=[6,15,7]

plt.plot(x,y,"g",label="Data1",linewidth=5,linestyle='dotted')
plt.plot(x1,y1,"r",label="Data2",linewidth=5,linestyle='dashed')

plt.title("Sample Data")
plt.xlabel("Tempreture")
plt.ylabel("Humidity")
plt.legend()
plt.grid(True,color="m")
plt.show()







