# ！／user/bin/env python
import random
from datetime import datetime, timedelta

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

def write(path,arr,generateRows):
    rexcel = open_workbook(path)  # 用wlrd提供的方法读取一个excel文件
    rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
    excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
    xf_style = xlwt.XFStyle()
    xf_style.num_format_str = 'yyyy/mm/dd hh:mm:ss'
    today = datetime.today()
    for row in range(generateRows): # 生成2万行数据
        column = 0
        for item in arr:
            # 最后一个元素直接赋值
            if item == arr[arr.__len__()-1]:
                table.write(rows, column, item)  # xlwt对象的写方法，参数分别是行、列、值
            elif str == type(item):
                table.write(rows, column, item + str(row))  # xlwt对象的写方法，参数分别是行、列、值
            elif datetime == type(item):
                table.write(rows, column, today,xf_style)  # xlwt对象的写方法，参数分别是行、列、值
            elif int == type(item):
                table.write(rows, column, str(round(int(item) * random.random() * 10,2)))  # xlwt对象的写方法，参数分别是行、列、值
            column += 1
        rows += 1
    excel.save("C:\\Users\\1\\Downloads\\collection.xls")  # xlwt对象的保存方法，这时便覆盖掉了原来的excel

if __name__ == '__main__':
    # xlsx 路径
    rows1 = 20
    rows2 = 2000
    today = datetime.today()
    # 项目基本信息
    xmjbxx_arr = ["项目编码","项目名称","项目概况",today,today,"白云区",100,"建设单位","发改委","发改委",today,201806]
    xmjbxx_map={"path":"C:\\Users\\1\\Downloads\\项目基本信息_采集模板.xlsx","arr":xmjbxx_arr}

    # 广州市房地产市场月报表
    gzsfdcscybb_arr = ["主键","类型",today,"地区",100,200,300,400,500,600,700,800,201806]
    gzsfdcscybb_map={"path":"C:\\Users\\1\\Downloads\\广州市房地产市场月报表_采集模板.xls","arr":gzsfdcscybb_arr}

    out_map = xmjbxx_map
    # 调用方法
    write(out_map["path"],out_map["arr"],rows2)


