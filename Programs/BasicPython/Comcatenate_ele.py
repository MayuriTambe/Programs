list=[]
Elements=int(input("Enter the number of elements in list:"))
for i in range(0,Elements):
    value=input("Enter the elements:")
    list.append(value)
def concatenate(list):
    new_string= ''
    for element in list:
        new_string += str(element)
    return new_string

print(concatenate(list))