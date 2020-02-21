import os.path
import time

FileName=(__file__)
print("The file name is:",FileName)
AccessTime=(time.ctime(os.path.getatime(__file__)))
print("The Accessing Time of file is:",AccessTime)
ModifyTime=(time.ctime(os.path.getmtime(__file__)))
print("The Modification Time of file is:",ModifyTime)
SizeOfFile=(os.path.getmtime(__file__))
print("The size of file is:",SizeOfFile)

