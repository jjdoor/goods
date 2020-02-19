# -*- coding: utf-8 -*-
import MySQLdb
import time
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



class TwitchFeaturedPipeline(object):

    # 初始化连接数据库
    def __init__(self):
        dbparams = {
            'host': '192.168.33.133',
            'port': 3306,
            'user': 'root',
            'password': 'yMTahf](OmtIBo(OQ,np1PViu8uUrWbD',
            'database': 'analysis',
            'charset': 'utf8'

        }
        self.conn = MySQLdb.connect("192.168.33.133", "root", "yMTahf](OmtIBo(OQ,np1PViu8uUrWbD", "analysis", charset='utf8')

        # self.conn = MySQLdb.Connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    # 使用property装饰器，方便sql语句的调用
    @property
    def sql(self):
        if not self._sql:
            self._sql = '''
                insert into jd(id, name, is_jd, url, sale_status,sale_time, created_time, updated_time) 
                values(null, "%s", %s, "%s", %s, "%s", "%s", "%s")
            '''
        return self._sql

    # 写入数据
    def process_item(self, item, spider):
        name = item['name']
        if item['sale_status'] == '距结束':
            sale_status = 0
        elif item['sale_status'] == '距开始':
            sale_status = 1
        else:
            sale_status = -1
        if item['source'] == '自营':
            is_jd = 1
        elif item['source'] == '备件库自营':
            is_jd = 1
        else:
            is_jd = 0
        url = item['href']
        created_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
        updated_time = created_time

        if sale_status == -1:
            sale_time = "0000-00-00 00:00:00"
        else:
            hour = int(item['hour'])
            minute = int(item['minute'])
            second = int(item['second'])

            t = time.time()
            t = t + hour * 3600 + minute * 60 + second
            # s = str(t)
            # sale_time = s[0:10]
            sale_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))

        # sql = "insert into jd(name, is_jd, url, sale_status,sale_time, created_time, updated_time) values(%s, %s, %s, %s, %s, %s, %s)"
        time_ = self.sql % (name, is_jd, url, sale_status, sale_time, created_time, updated_time)
        print "---------------------"+time_+"-------------------------"
        self.cursor.execute(time_)
        self.conn.commit()

        return item
