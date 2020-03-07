def cloning(list1):
    list_copy=[]
    for element in list1:
        list_copy.append(element)
    return list_copy
list1=[5,7,3,6,2,8]
list2=cloning(list1)
print("Original list:",list1)
print("The list after cloning is:",list2)