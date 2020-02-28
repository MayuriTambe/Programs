import numpy as np

Array_Elements=np.array([(10 ,20 ,30 ,40 ,50, 60, 70, 80, 90, 100)])
print("The Array is before removing elements: \n",Array_Elements)

Position=(1,4,5)

New_Array=np.delete(Array_Elements,Position)
print("After removing the elements at specific position the Array is:\n",New_Array)


