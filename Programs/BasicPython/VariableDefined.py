try:
    value1= 10
except NameError:
    print("value1 is not defined....")
else:
    print("value1 is defined.")
try:
    value2
except NameError:
    print("value2 is not defined....")
else:
    print("value2 is defined.")

