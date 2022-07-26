import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="PpHRSN_2022",database="prasannadb")

mycursor=mydb.cursor()
#create table
#mycursor.execute("Create database samdb")
mycursor.execute("Create table python_employee (emp_id int(200),name varchar(20),photo BLOB,biodataFile varchar(20))")


mycursor.executemany(sqlform,employee)

mydb.commit()
