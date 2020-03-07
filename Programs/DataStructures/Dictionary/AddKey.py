#Add key to the Dictionary

names={1:"john",2:"max",3:"Justin"}
print("The Dictionary is:",names)

keys=int(input("Enter the keys to be added:"))
value=input("Enter the value")

if keys not in names:
    names[keys]=value
else:
    print("key is already exist")
print(names)