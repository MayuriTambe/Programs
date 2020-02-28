import pandas as pd
First_Sample=pd.Series ([2, 4, 6, 8, 10])
Second_Sample=pd.Series([1, 3, 5, 7, 9])

Addition=First_Sample+Second_Sample
print("The Addition of Two series are\n",Addition)

Substraction=First_Sample-Second_Sample
print("The Substraction of Two series are\n",Substraction)

Multiplication=First_Sample*Second_Sample
print("The Multiplication of Two series are\n",Multiplication)

Division=First_Sample/Second_Sample
print("The division of Two series are\n",Division)