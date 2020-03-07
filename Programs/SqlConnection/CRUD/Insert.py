import mysql.connector
database=mysql.connector.connect(host="localhost", user="admin1", passwd="admin123", database="codes")
mycursor=database.cursor()

query="INSERT INTO EMPLOYEE (NAME,AGE,PERSONAL_ID) VALUES(%s,%s,%s)"
Data1=("Rakesh",54,197)

mycursor.execute(query,Data1)
database.commit()


for x in mycursor:
    print(x)