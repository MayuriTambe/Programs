import numpy as np

Sample_Array=np.array([10,20,30,40,50,60]).reshape(2,3)
print("The Array before Adding Columbn is:\n",Sample_Array)
New_Array=np.array([[100],[200]])
ColumnAddition=np.append(Sample_Array,New_Array,1)
print("The Array After Adding Columbn is:\n",ColumnAddition)