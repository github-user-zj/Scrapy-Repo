# -*- coding: utf-8 -*-

"""
__title__ = '连接数据库管道'
__author__ = 'zhangjun'
__mtime__ = '2017/3/15'

"""
import MySQLdb

class LbldyPipeline(object):
    def process_item(self, item, spider):
        conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='spider_demo',charset='utf8')
        cursor = conn.cursor()
        insert_sql = "insert into lbl_db(name,summary,link,website) VALUES('{0}','{1}','{2}','{3}')".\
            format(item['dy_name'],item['dy_summary'],item['dy_link'],item['dy_websit'])
        cursor.execute(insert_sql)
        conn.commit()