import mysql.connector
database=mysql.connector.connect(host="localhost", user="admin1", passwd="admin123", database="codes")
mycursor=database.cursor()

query="update EMPLOYEE set NAME='Sunil' where NAME='Nirav'"
try:
    mycursor.execute(query)
    print("Updated Succesfully")
except:
    print("Not succesfully updated")
database.commit()
