#coding:utf-8
import MySQLdb
import time

# 打开数据库连接
db = MySQLdb.connect("192.168.33.133", "root", "yMTahf](OmtIBo(OQ,np1PViu8uUrWbD", "analysis", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
sql = "insert into test(name) value('1')"
# cursor.execute("SELECT VERSION()")
cursor.execute(sql)
db.commit()

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
# dataa = cursor.fetchall()

print data

# 关闭数据库连接
db.close()