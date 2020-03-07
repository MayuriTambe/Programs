Name_of_String=input("Enter the String")
length=len(Name_of_String)
if length>2:
    if Name_of_String[-3:]=="ing":
        Name_of_String+="ly"
    else:
        Name_of_String+="ing"
print(Name_of_String)