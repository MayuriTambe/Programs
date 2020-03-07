#Nested Dictionaries

Data={"Dict1":{1:"red",2:"Green"},"Dict2":{4:"yellow",6:"Brown"}}
print(Data)
try:
    print(Data["Dict1"])
    print(Data["Dict2"][4])
except:
    print("Not found")