import calendar

#Using calender function calculate month and year

no_of_month=int(input("Enter the month"))
no_of_year=int(input("Enter the year:"))

calenderRecords=(calendar.month(no_of_year,no_of_month))
print(calenderRecords)

