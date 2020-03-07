string=input("Enter the String")
print("The String is:",string)
def characterOccurence(string):
    dict = {}
    for element in string:
        keys = dict.keys()
        if element in keys:
            dict[element] += 1
        else:
            dict[element] = 1
    return dict
print("The dictionary is:",characterOccurence(string))
