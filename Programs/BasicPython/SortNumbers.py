First_number = int(input("Input first number: "))
Second_number= int(input("Input second number: "))
Third_number= int(input("Input third number: "))

Minimum = min(First_number,Second_number,Third_number)
Maximum= max(First_number, Second_number, Third_number)
MidNumber = (First_number + Second_number + Third_number) - Minimum - Maximum
print("Numbers in sorted order: ", Minimum, MidNumber,Maximum)