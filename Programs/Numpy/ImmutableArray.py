import numpy as np

value=np.zeros(6)
value.flags.writeable=False
print("Test the array is read-only or not:")
print("Try to change the value of the first element:")
value[0] = 1
