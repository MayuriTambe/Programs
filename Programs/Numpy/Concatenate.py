import numpy as np

First_Array=np.array([[0, 1, 3], [5, 7, 9]])
print(First_Array)
Second_Array=np.array([[0, 2, 4], [6, 8, 10]])
Concatenate=np.concatenate((First_Array,Second_Array),1)
print("The comcatenation of two array is:\n",Concatenate)