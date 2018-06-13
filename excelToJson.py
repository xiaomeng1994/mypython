#！／user/bin/env python
#-*- coding:utf-8 -*-
import xlrd
from collections import OrderedDict
import json
import codecs

# excel转json小工具

# xlsx 路径
path = "C:\\Users\\1\\Desktop\\tmp\\c3.xlsx"
# 获取文件名称,把输出json放在该目录下
jsonPath=path[:path.index(".")]+".json"
print(jsonPath)
# 打开excel
wb = xlrd.open_workbook(path)

convert_list = []
# 拿第一个sheet
sh = wb.sheet_by_index(0)
# 取第一行为字段名
title = sh.row_values(0)
# 编列行
for rownum in range(1, sh.nrows):
    rowvalue = sh.row_values(rownum)
    single = OrderedDict()
    # 遍历列
    for colnum in range(0, len(rowvalue)):
        #打印字段名称，字段值
        #print(title[colnum], rowvalue[colnum])
        single[title[colnum]] = rowvalue[colnum]
    convert_list.append(single)

# 将list集合，转换成json格式，参数：ensure_ascii 解决中文乱码
j = json.dumps(convert_list, ensure_ascii=False)

with codecs.open(jsonPath, "w", "utf-8") as f:
    f.write(j)
    f.close()