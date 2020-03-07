Data=(22,54,11,66,4,8,55,22,54,8,4)
print("The tuple is:",Data)
for i in range(0,len(Data)):
    for j in range(i+1,len(Data)):

        if Data[i]==Data[j]:
            print(Data[i])



