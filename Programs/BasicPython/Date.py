#To Calculate the no of Days for specific date
from datetime import date

value1=date(2020,7,29)
value2=date(2020,10,11)

Result=value2-value1
print(Result.days,"Days")

