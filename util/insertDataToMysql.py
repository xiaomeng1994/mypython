#！/user/bin/env python
#-*- coding:utf-8 -*-

# 插入数据到mysql
import pymysql


def insertDataToMysql(sql, sql_list):
    # 建立mysql连接
    conn = pymysql.connect(
        host='hd2',
        user='root',
        passwd='root',
        # db='myspringboot',
        db='hqwswlwjd',
        port=3306,
        charset='utf8'
    )

    # 获得游标
    cur = conn.cursor()
    #cur.executemany(sql, sql_list)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()