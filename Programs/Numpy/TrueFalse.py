import numpy as np

First_Array=np.array([1,2])
print("The first Array is:\n",First_Array)

Second_Array=np.array([4,5])
print("The Second Array is:\n",Second_Array)

Greater=np.greater(First_Array,Second_Array)
print("The First_Array is greater than Second_Array is:\n",Greater)

GreaterEqual=np.greater_equal(First_Array,Second_Array)
print("The First_Array is greater than equal to Second_Array is:\n",GreaterEqual)

less=np.less(First_Array,Second_Array)
print("The First_Array is less than Second_Array is:\n",less)

LessEqual=np.less_equal(First_Array,Second_Array)
print("The First_Array is less than equal to Second_Array is:\n",LessEqual)
