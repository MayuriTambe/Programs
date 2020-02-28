import numpy as np

Sample_Array=np.array([2,4,6,6,8,10]).reshape(2,3)
print("The Sample Array is:\n",Sample_Array)
DataType=Sample_Array.dtype
print("The Data Type is:\n",DataType)
ChangeDataType=Sample_Array.astype(float)
print(ChangeDataType)
print("The Data Type is:\n",ChangeDataType.dtype)

