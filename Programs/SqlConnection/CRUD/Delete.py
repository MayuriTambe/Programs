import pymysql
database = pymysql.connect("localhost", "admin1", "admin123", "codes")
mycursor=database.cursor()

query="delete from EMPLOYEE where NAME='John'"
mycursor.execute(query)
database.commit()
