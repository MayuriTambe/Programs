#Calculate the character of string in form Dictionaries
string=input("Enter the string")
character={}

for i in string:
    character[i]=character.get(i,0)+1
print("The Dictonary is;",character)