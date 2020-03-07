import mysql.connector
database =mysql.connector.connect(host="localhost", user="admin1", passwd="admin123", database="codes")
mycursor=database.cursor()

mycursor.execute("select * from EMPLOYEE")
result=mycursor.fetchall()
database.commit()
for res in result:
    print(res)
