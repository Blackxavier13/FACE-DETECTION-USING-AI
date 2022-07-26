import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="PpHRSN_2022",database="prasannadb")

mycursor=mydb.cursor()
#create table
#mycursor.execute("Create database samdb")
#mycursor.execute("Create table employee (name varchar(200),sal int(20))")

sqlform="Insert into employee (name,sal) values(%s,%s)"
employee =[("Praveena", 8000),("Jenny", 10000), ("Joshua",15000)]

mycursor.executemany(sqlform,employee)

mydb.commit()
