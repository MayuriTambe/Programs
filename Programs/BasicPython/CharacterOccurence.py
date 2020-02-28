from array import *

string=input("Enter the string:")
character=input("Enter the character:")
print(string)
count=0
for i in string:
    if i==character:
        count+=1
print("The Occurence of entered character is:",str(count))



