import pymysql
database = pymysql.connect("localhost", "admin1", "admin123", "codes")
mycursor=database.cursor()

mycursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql ='''CREATE TABLE EMPLOYEE(
   NAME CHAR(20) NOT NULL,
   AGE INT,PERSONAL_ID INT PRIMARY KEY AUTO_INCREMENT
)'''
mycursor.execute(sql)
print("Table Created")


database.close()