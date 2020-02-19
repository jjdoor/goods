import pymysql

db=pymysql.connect("localhost","root","","test")
cursor = db.cursor()
cursor.execute("select * from test")
fetchone = cursor.fetchall()
print(fetchone)
db.close()
