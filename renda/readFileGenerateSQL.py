# 过滤掉所有空行文件
import pymysql


def check_contain_chinese(check_str):
    # for ch in check_str.decode('utf-8'): # 不需要编码为utf8
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def test(data):
    sql_1 = 'insert into gzrd_sjcj_yhxxb(YHNC,YHM,MM,SSBM,SSGW,JS,SJHM,DZYX)VALUES ("%s","%s","%s","%s","%s","%s",%s,%s);' % (
    data[0], data[1], data[2], data[3], data[4], data[5], data[6], '""')
    print(sql_1)

def insertData(data):
    connection = pymysql.connect(host='hd2',
                                 user='root',
                                 password='root',
                                 db='renda',
                                 port=3306,
                                 charset='utf8')  # 注意是utf8不是utf-8
    try:
        with connection.cursor() as cursor:
            sql_1 = 'insert into gzrd_sjcj_yhxxb(YHUNC,YHM,MM,SSBM,SSGW,JS,SJHM,DZYX)VALUES ("%s","%s","%s","%s","%s","%s",%s,%s)' % (data[0], data[1], data[2], data[3], data[4], data[5], data[6],'""')
            print(sql_1)
            cursor.execute(sql_1)

            connection.commit()
    finally:
        connection.close()

if __name__ == '__main__':
    i = 1
    for line in open("d:/tmp/tmp.log", 'r',encoding='utf-8').readlines():
        if line.strip() != '':
            #print(line.rstrip())
            print('(\''+line.rstrip().split("\t")[0]+'\','+'\''+line.rstrip().split("\t")[1]+'\'),')
            #print(("update gzrd_sjcj_bmxxb set BMBM='%s' where BMBM = '" + line.rstrip() + "'") % ("BMBM_0"+str(i)))
            #split = line.rstrip().split("\t")
            #print(split)
            #split = line.rstrip().split("\t")
            #print("INSERT INTO gzrd_sjcj_bmcdglb (`XH`, `BMBM`, `CDBM`, `CJSJ`)VALUES ('%s','%s', '%s', '%s');" % (str(i),split[0],split[1],split[2]))
            i += 1


