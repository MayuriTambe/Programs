
Str1=input("Enter the string to be converted uppercase: ")

for i in range (0,len(Str1)):

   character=ord(Str1[i])
   if character>=97 and character<=122:
       character=character-32
   else:
       character=character+32
   Convert=chr(character)
   print(Convert,end="")