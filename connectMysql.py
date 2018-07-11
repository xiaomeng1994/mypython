#!/usr/bin/python3

# -*- coding: UTF-8 -*-
import pymysql.cursors

connection = pymysql.connect(host='hd1',
                             user='root',
                             password='root',
                             db='myspringboot',
                             port=3306,
                             charset='utf8')  # 注意是utf8不是utf-8
try:
    with connection.cursor() as cursor:
        sql_1 = 'select * from u_user'
        cout_1 = cursor.execute(sql_1)
        print("数量： " + str(cout_1))
        for row in cursor.fetchall():
            print("id:", str(row[0]), 'name', str(row[1]), 'age', str(row[2]))

        #sql_2 = 'insert into u_user(userId,age,gender,occupation) value(9527,26,"F","student")'
        sql_2 = 'delete from u_user where userId="9527"'
        cout_2 = cursor.execute(sql_2)
        print("数量： " + str(cout_2))
        connection.commit()
finally:
    connection.close()



