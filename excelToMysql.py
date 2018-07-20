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
    file_list = [
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/19.遣送出境外国人情况--国籍前五位.xlsx',1,'hqwsw_qscjwgrqk_gjqww'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/18.遣送出境外国人情况--按市辖区分.xlsx',1,'hqwsw_qscjwgrqk_asxqf'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/17.查处“三非”外国人情况--按违法事项分.xlsx',1,'hqwsw_ccsfwgrqk_awfsxf'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/16.查处“三非”外国人情况--国籍前五位.xlsx',1,'hqwsw_ccsfwgrqk_gjqww'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/15.查处“三非”外国人情况--按市辖区分.xlsx',1,'hqwsw_ccsfwgrqk_asxqf'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/14.实有外国人情况--国籍前五位.xlsx',1,'hqwsw_sywgrqk_gjqww'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/13.实有外国人情况--按大洲分.xlsx',1,'hqwsw_sywgrqk_adzf'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/12.实有外国人情况--按市辖区分.xlsx',1,'hqwsw_sywgrqk_asxqf'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/11.住宿登记情况--国籍前五位.xlsx',1,'hqwsw_zsdjqk_gjqww'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/10.住宿登记情况--按大洲分.xlsx',1,'hqwsw_zsdjqk_adzf'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/9.住宿登记情况--按市辖区分.xlsx',1,'hqwsw_zsdjqk_asxqf'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/8.刑拘越南人情况统计表.xlsx',1,'hqwsw_xjynrqk'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/7.中小学在读外国学生情况统计表.xlsx',1,'hqwsw_zxxzdwgxsqk'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/6.小孩出生情况统计表.xlsx',1,'hqwsw_xhcsqk'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/5.离婚登记情况统计表.xlsx',1,'hqwsw_lhdjqk'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/4.结婚登记情况统计表.xlsx',1,'hqwsw_jhdjqk'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/3.传染病情况统计表.xlsx',1,'hqwsw_crbqk'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/2.报列不准入境情况统计表.xlsx',1,'hqwsw_blbzrjqk'),
        ('C:/Users/1/Desktop/广州人大/整理/文档管理/智慧人大/8_涉外管理联网监督系统/清洗后的数据/1.入境外国人情况统计表.xlsx',1,'hqwsw_rjwgrqk')]

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


