str=input("Enter the string")#Take a string
replace=str[0]
def ReplaceString(str):#Defining function

    Result= str.replace(replace,"$")
    Result = replace + Result[1:]
    #Using string replace function to replace string.
    print("The Replace String is=",Result)#Display the result

ReplaceString(str )
