import array as arr

class ReverseArray:
    pass
def reverse():
    new_array=arr.array("i",[6,4,8,2,8,1])
    print("The array is:",new_array)
    reverse_array=new_array[::-1]
    print("The reverse array is:",reverse_array)

reverse()
