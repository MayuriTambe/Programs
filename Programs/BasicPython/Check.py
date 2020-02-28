#Check the number in list exist or not

list=[]
Elements=int(input("Enter the no of elements:"))
for i in range(0,Elements):
    Value=int(input("Enter the Elements:"))
    list.append(Value)


Search_number=int(input("Enter the number you want to search in list:"))
if Search_number in list:
    print("true")
else:
    print("false")
