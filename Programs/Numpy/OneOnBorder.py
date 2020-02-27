import numpy as np

Ones_Array=np.ones((5,5))
print("The Array is :",Ones_Array)
Ones_Array[1:-1]=0
print("Adding Zeros in middle of matrix:\n",Ones_Array)