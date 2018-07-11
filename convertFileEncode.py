#!/usr/bin/python3

# -*- coding: UTF-8 -*-

import os
import sys
import codecs


# 该程序用于将目录下的文件从指定格式转换到指定格式，默认的是GBK转到utf-8
def convert(file, in_enc="GBK", out_enc="UTF-8"):
    try:
        print("convert " + file)
        f = codecs.open(file, 'r', in_enc)
        new_content = f.read()
        codecs.open(file, 'w', out_enc).write(new_content)
        # print (f.read())
    except IOError as err:
        print("I/O error: {0}".format(err))


def explore(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            convert(path)


def main():
    for path in sys.argv[1:]:
        main2(path)

def main2(path):
    if (os.path.isfile(path)):
        convert(path)
    elif os.path.isdir(path):
        explore(path)

if __name__ == "__main__":
    path='D:\\soft\\jetbrains\\project\\idea\\thread\\src\\main\\java\\com\\roocon\\thread'
    main2(path)