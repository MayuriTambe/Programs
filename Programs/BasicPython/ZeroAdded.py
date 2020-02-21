
string = input("Enter the String")
NoOfZeros = int(input("Enter the Number Of zeroes to be Added"))

def ZeroAdded(self,string,NoOfZeros):
    NewString=string.zfill(NoOfZeros+len(string))
    print("The Zeroes Added String is;",NewString)
ZeroAdded()
