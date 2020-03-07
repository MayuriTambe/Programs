from array import *

arr=[4,6,3,8,4,8,1,2,4,9,6,8,3]

element=int(input("Enter the element"))
print(arr)
def Occurence(arr,element):
    count=0
    j=0

    for j in arr:
        if j==element:
            count=+1
            j=+1

    print(count)
Occurence(arr,element)



