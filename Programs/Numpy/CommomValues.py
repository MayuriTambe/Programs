import numpy as np

Array1= np.array([0 ,10, 20, 40, 60])
Array2=np.array([10, 30, 40])
for val1 in Array1:
    for val2 in Array2:
        if val1==val2:
            print(val1)
#By Using numpy function
print("The common elements from both arrays are:",np.intersect1d(Array1,Array2))