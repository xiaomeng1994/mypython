#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import util.readExcel as rExcel
import util.pinyinutil as pinyin
import util.insertDataToMysql as dMysql

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
    file_list = [
        ('C:/Users/1/Desktop/清洗后的数据/15.查处“三非”外国人情况--按市辖区分.xlsx',1,'hqwsw_ccsfwgrqk_asxqf'),
        ('C:/Users/1/Desktop/清洗后的数据/14.实有外国人情况--国籍前五位.xlsx',1,'hqwsw_sywgrqk_gjqww'),
        ('C:/Users/1/Desktop/清洗后的数据/13.实有外国人情况--按大洲分.xlsx',1,'hqwsw_sywgrqk_adzf'),
        ('C:/Users/1/Desktop/清洗后的数据/12.实有外国人情况--按市辖区分.xlsx',1,'hqwsw_sywgrqk_asxqf'),
        ('C:/Users/1/Desktop/清洗后的数据/11.住宿登记情况--国籍前五位.xlsx',1,'hqwsw_zsdjqk_gjqww'),
        ('1.入境外国人情况统计表.xlsx',1,'hqwsw_rjwgrqk'),('用户.xlsx',0,'user'),('test.xlsx',0,'u')]
    data_list = rExcel.readExcel(file_list[0][0], file_list[0][1])
    to_pinyin = chinese_to_pinyin(data_list.pop(0))
    print(to_pinyin)
    # sql = ('INSERT INTO %s(%s) VALUE %s' %(file_list[0][2],','.join(to_pinyin),str(('%s',)*to_pinyin.__len__()).replace("'","")))
    # print(sql)
    for tup in data_list:
        sql = ('INSERT INTO %s(%s) VALUES %s' % (file_list[0][2], ','.join(to_pinyin), str(tup).replace("None","NULL")))
        print(sql)
        dMysql.insertDataToMysql(sql,'')


