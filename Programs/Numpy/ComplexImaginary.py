import numpy as np

First_Array=np.sqrt([1+0j])
Second_Array= np.sqrt([0+1j])
print(First_Array,Second_Array)

RealPart=First_Array.real
print("The Real part of first_Array  is:",RealPart)

ImaginaryPart=First_Array.imag
print("The Imaginary part of First_Array  is:",ImaginaryPart)

RealPart=Second_Array.real
print("The Real part of Second_Array  is:",RealPart)

ImaginaryPart=Second_Array.imag
print("The Imaginary part of Second_Array is:",ImaginaryPart)