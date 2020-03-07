#Multiplis the Elements in list

Data = [2, 4, 5, 3, 3, 6]
print("The list is:", Data)

def Multiply(Data):
    Result = 1
    for i in Data:
        Result=Result*i
    return  Result

print(Multiply(Data))


