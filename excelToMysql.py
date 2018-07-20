#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import util.read_excel as rExcel
import util.pinyinutil as pinyin
import util.excute_to_mysql as dMysql

def chinese_to_pinyin(arr):
    data_list = []
    # 字符串数组
    for data in arr:
        # 遍历字符串，拿到每个汉字
        cell_ata = ''
        for c in data:
            cell_ata += pinyin.to_pinyin(c)[:1].upper()
        data_list.append(cell_ata)
    return data_list



if __name__ == '__main__':
    file_list = [('C:/test.xlsx',1,'test')]
    index = 15
    # for index in  range(file_list.__len__()):
    print(index)
    data_list = rExcel.readExcel(file_list[index][0], file_list[index][1])
    to_pinyin = chinese_to_pinyin(data_list.pop(0))
    print(to_pinyin)
    # 先刪除表数据
    dMysql.insertDataToMysql("truncate table " + file_list[index][2], "")
    for tup in data_list:
        sql = ('INSERT INTO %s(%s) VALUES %s' % (file_list[index][2], ','.join(to_pinyin), str(tup).replace("None","NULL")))
        print(sql)
        # 插入数据
        dMysql.insertDataToMysql(sql,file_list[index][2])


