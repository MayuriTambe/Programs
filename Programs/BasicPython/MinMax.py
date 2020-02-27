def Maximum_Minimum(value):
    Maximum_number=value[0]
    Minimum_number=value[0]

    for number in value:
        if number > Maximum_number:
            Maximum_number=number
        elif number < Minimum_number:
            Minimum_number=number
    return Maximum_number,Minimum_number

print(Maximum_Minimum([34,56,22,86,34,77,5,11]))
