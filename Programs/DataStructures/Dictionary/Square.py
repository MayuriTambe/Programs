#print the value in form of square of key

value=int(input("Enter the number to specific range"))
square={}

for element in range(0,value+1):
    square[element]=element*element
print(square)

