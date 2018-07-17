#!/usr/bin/python3

# -*- coding: UTF-8 -*-

#
# 修改数据采集目录模版
#

import re

import pymysql.cursors

def connectMysql(tableName):
    connection = pymysql.connect(host='hd2',
                                 user='root',
                                 password='root',
                                 db='renda',
                                 port=3306,
                                 charset='utf8')  # 注意是utf8不是utf-8
    try:
        with connection.cursor() as cursor:
            sql_1 = 'desc ' + tableName.lower()
            cursor.execute(sql_1)
            i = 0
            data = cursor.fetchall()
            column = ""
            for row in data:
                i = i + 1
                if i == data.__len__():
                    continue
                elif str(row[1]).__contains__("varchar"):
                    column += ("文字描述，最长" + str(int(re.sub("\D", "", str(row[1]))) / 2)[:-2] + "个文字") + "\t"
                elif str(row[1]).__contains__("decimal"):
                    column += ("数字格式，最多保留" + str(row[1][-2:-1]) + "位小数") + "\t"
                elif str(row[1]).__contains__("int"):
                    column += ("整数格式，最长" + str(row[1][-2:-1]) + "位数") + "\t"
                elif str(row[1]).__contains__("datetime"):
                    # print(" ".rstrip()+"\t" )
                    column += "日期格式，如2018年1月1日，则输入2018/1/1" + "\t"
            print(column[:-1])
    finally:
        connection.close()


if __name__ == '__main__':
    tableNames = (
        ('项目基本信息', 'CXJW_XMJBXX'),
        ('广州市房地产市场月报表', 'CXJW_GZSFDCSCYBB'),
        ('工程报监基本情况表明细', 'CXJW_GCBJJBQKBMX'),
        ('重点城建项目工作进度情况表', 'CXJW_ZDCJXMGZJDQKB'),
        ('城市更新项目市财政资金进度表', 'CXJW_CSGXXMSCZZJJDB'),
        ('低值可回收物回收量报表', 'CXJW_DZKHSWHSLBB'),
        ('中心城区生活垃圾无害化处理情况', 'CXJW_ZXCQSHLJWHHCLQK'),
        ('生活垃圾分类进展情况报表', 'CXJW_SHLJFLJZQKBB'),
        ('生活垃圾焚烧处理量', 'CXJW_SHLJFSCLL'),
        ('违法建设治理情况', 'CXJW_WFJSZLQK'),
        ('市管道燃气三年提升任务完成情况', 'CXJW_SGDRQSNTSRWWCQK'),
        ('市容环境卫生管理类执法情况', 'CXJW_SRHJWSGLLZFQK'),
        ('白云山风景区进园人次统计表', 'CXJW_BYSFJQJYRCTJB'),
        ('白云山风景区红线范围内违法占地违法建设行为统计表', 'CXJW_BYSFJQHXFWNWFZDWFJSXWTJB'),
        ('重点整治河涌水质监测信息', 'CXJW_ZDZZHYSZJCXX'),
        ('广州市空气质量日报', 'CXJW_GZSKQZLRB'),
        ('广州市林木资源主要数据统计表', 'CXJW_GZSLMZYZYSJTJB'),
        ('广州市生态公益林主要数据统计表', 'CXJW_GZSSTGYLZYSJTJB'),
        ('广州市森林公园分布情况表', 'CXJW_GZSSLGYFBQKB'),
        ('广州市森林公园发展情况表', 'CXJW_GZSSLGYFZQKB'),
        ('广州市主要园林绿化统计表', 'CXJW_GZSZYYLLHTJB'),
        ('广州市城市公园发展情况表', 'CXJW_GZSCSGYFZQKB'),
        ('广州市绿道建设情况表', 'CXJW_GZSLDJSQKB'),
        ('广州市湿地公园统计表', 'CXJW_GZSSDGYTJB'),
        ('污水管网建设项目进展情况一览表', 'CXJW_WSGWJSXMJZQKYLB')
    )
    for i in tableNames:
        print(i[0])
        connectMysql(i[1])
        print()