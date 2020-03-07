marks={4,3,5,6,7,2,9,44,5}
maximum={}
minimum={}

for number in marks:
    if number.issuperset(maximum):#number.is
        maximum=number
    elif number<minimum:
        minimum=number
print("The minimum number is:",minimum)
print("The maximum number is:",maximum)



