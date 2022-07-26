import pymysql
def mysqlconnect():
    connection =pymysql.connect(host='database-2.cluster-cmqzznawwnnt.us-east-1.rds.amazonaws.com',
        user='admin',
        password='admin123',
        database='mysqldb')
    with connection :
        cur = connection.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
    print("Database version:{}".format(version[0]))
if __name__ == "__main__":
    mysqlconnect()