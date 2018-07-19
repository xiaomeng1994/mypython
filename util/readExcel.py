#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xlrd
import openpyxl
import openpyxl.cell.cell

# it must be installed xlrd

# 读取excel的数据
#
#
def readExcel(file_path,start_row):
    # 数据数组
    data_list = []
    # 打开excel
    book = openpyxl.load_workbook(file_path,read_only=True,data_only=True)
    if book.worksheets.__len__() != 1:
        print(file_path)
    else:
        # 获取到第一个sheet
        sheet = book.worksheets.__getitem__(0)
        for row in sheet.rows:
            values = []
            for cell in row:
                cell_value = cell.value
                if str(cell_value).strip() == '':
                    cell_value = None
                elif '0.00%' == cell.number_format and (type(cell_value) == int or type(cell_value) == float):
                    cell_value = round(cell_value*100, 2)
                elif type(cell_value) == float:
                    cell_value = round(cell_value, 2)
                values.append(cell_value)
            data_list.append(tuple(values))
    # 删除前面不要的数据
    for i in range(start_row):
        if data_list.__len__() > 0:
            data_list.pop(0)
    return data_list
