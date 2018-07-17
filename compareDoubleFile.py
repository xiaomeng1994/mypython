# 对比两个文件不存在的内容
if __name__ == '__main__':
    tmp1 = list()
    tmp2 = list()
    for line in open("d:/tmp/tmp.log", 'r',encoding='utf-8').readlines():
        if line.strip() != '':
            tmp1.append(line.rstrip().lower())

    for line in open("d:/tmp/tmp2.log", 'r',encoding='utf-8').readlines():
        if line.strip() != '':
            tmp2.append(line.rstrip().lower())

    if tmp2.__len__() > tmp1.__len__():
        for i in tmp2:
            if not tmp1.__contains__(i):
                print(i)
    else:
        for i in tmp1:
            if not tmp2.__contains__(i):
                print(i)
    print(tmp1)
    print(tmp2)