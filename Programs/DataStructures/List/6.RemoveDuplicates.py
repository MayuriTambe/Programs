values=[1,3,5,4,6,7,8,5,3]
print("The list is:",values)

dup=[]
for i in values:
    if i not in dup:
        dup.append(i)
print("After removing duplicates list is:",dup)

