import os

import util.pinyinutil as pinyin

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
    file_name_list = []
    for line in open("d:/tmp/tmp.log", encoding='utf8'):
        #print("".join(chinese_to_pinyin(line.rstrip())))
        if line.strip() != '':
            # print("'"+line.rstrip()+"',")
            file_name_list.append(line.strip())

    m = {}
    for f in os.listdir("C:/Users/1/Desktop/清洗后的数据"):
        if f.__contains__(".xlsx"):
            f_name = str(f)
            f_simple_name = f_name[f_name.find(".")+1:f_name.rfind(".")]
            pinyin_simple_name = "hqwsw_" + "".join(chinese_to_pinyin(f_simple_name.replace("--","_").replace("“","").replace("”","").replace("统计表",""))).lower()
            m[pinyin_simple_name] = f_simple_name
            print(pinyin_simple_name,f_name)

    for i in file_name_list:
        (m.get(i.lower()))

