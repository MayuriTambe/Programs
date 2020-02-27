import numpy as np

first_array=np.array([0,10,20,40,60,80])
print(first_array)
second_array=np.array([10, 30, 40, 50, 70])
print(second_array)
uniqueelements=np.setxor1d(first_array,second_array)
print("The set exclusive-or of two arrays:",uniqueelements)