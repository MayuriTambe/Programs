
list1=[]
Elements=int(input("Enter the number of elements in list:"))
for i in range(0,Elements):
    value=input("Enter the elements:")
    list1.append(value)
print(tuple(list1))
print(list(list1))


