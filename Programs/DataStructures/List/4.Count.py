Data=['abc', 'xyz', 'aba', '1221']
print("The list is:",Data)

Result=0

for element in Data:
    if element[0]==element[-1]:
        Result=+1

print(list.count(Result))


