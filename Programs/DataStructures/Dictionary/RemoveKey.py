#Remove key

names={1:"john",2:"max",3:"Justin",5:"Ronny"}
print("The Dictionary is:",names)

keys=int(input("Enter the keys to be remove:"))
if keys  in names:
    names.pop(keys)
else:
    print("The key you entered is not exist")
print("After removing the Dictionary is:",names)
