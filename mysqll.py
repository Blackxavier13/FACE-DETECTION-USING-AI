import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="PpHRSN_2022")

mycursor=mydb.cursor()
#create table

mycursor.execute("Show databases ")

for db in mycursor:
    print(db)