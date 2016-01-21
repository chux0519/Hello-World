# encoding:utf-8
import xlrd
from db import *
import time

ISOTIMEFORMAT = '%Y-%m-%d %X'


def config(middle_result_name, master_id, slave_id):
    # 进行初始化，获取表单的页码和行列数
    init_workbook = xlrd.open_workbook(middle_result_name)
    worksheet = init_workbook.sheets()[0]
    hight = worksheet.nrows
    print "hight:%s" % hight
    columns = worksheet.ncols
    print"columns:%s" % columns
    for i in range(0, columns):
        if worksheet.cell(0, i).value == '':
            master_info_stop = i - 1
            slave_info_start = i + 1
        elif worksheet.cell(0, i).value == master_id:
            master_id = i
        elif worksheet.cell(0, i).value == slave_id:
            slave_id = i
    print master_id, slave_id, master_info_stop, slave_info_start
    cur, conn = init_database('127.0.0.1', 'root', 'toor', 'mapper')
    log = open('target/config_log.txt', 'a')
    sql = "insert into task_config (middle_result_name,master_id,master_info_stop,slave_id,slave_info_start)  values('%s','%s','%s','%s','%s')" % (
        middle_result_name, master_id, master_info_stop, slave_id, slave_info_start)
    cur.execute(sql)
    conn.commit()
    # 写入日志前一定要字符串化信息
    string = sql + "$" + \
        time.strftime(ISOTIMEFORMAT, time.localtime()) + "\n"
    log.write(string)
    close(cur, conn)
    log.close()

if __name__ == '__main__':
    import sys
    config(sys.argv[1], sys.argv[2], sys.argv[3])
