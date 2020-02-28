import numpy as np

First_Array=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(First_Array)
number=3
Multiplied_Array=number*First_Array.reshape(3,4)
print("The multiplied Array ny number 3 is:\n",Multiplied_Array)