import numpy as np

Zeros_Array=np.zeros((5,5))
print("The Array is:\n",Zeros_Array)
Zeros_Array[1:-1,1:-1]=1
print("Adding 1 in the Matrix is;\n",Zeros_Array)