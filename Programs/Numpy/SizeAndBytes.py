import numpy as np

Data=np.array([12,33,2])
print("The Size of Array is:",Data.size)

ByteSize=Data.itemsize
print("The Byte Size of Array is:",ByteSize)

TotalByteSize=Data.nbytes
print("Total bytes consumed by the elements of the array:",TotalByteSize)