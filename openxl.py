# encoding:utf-8
# from openpyxl import load_workbook #该模块只支持xlsx
import xlrd

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Drug(object):
    """新建一个类，用来装每种药"""
    info = {}
    num = 0

    def __init__(self, info, num):
        self.info = info
        self.num = num


def openxl(name):
    # 进行初始化，获取表单的页码和行列数
    init_workbook = xlrd.open_workbook(name)
    worksheet = init_workbook.sheets()[0]
    hight = worksheet.nrows
    print "hight:%s" % hight
    columns = worksheet.ncols
    print"columns:%s" % columns
    # 开始处理，从第二行到最后一行
    package = []
    data = {"master": {}, "slave": []}
    for i in range(1, hight):
        # 划分依据：1.有被匹配药物	2.连续被匹配药物的比配对象相同
        if worksheet.cell(i, 23).value != '':
            print "i,23:%s" % worksheet.cell(i, 23).value
            # 初始化主从药物的key，value，方便后面进一步对其进行打包
            # 左边比对药物为master，右边匹配出的结果为slave
            master_key = []
            master_value = []
            slave_key = []
            slave_value = []
            # master药物的有效信息是4,10
            for j in range(4, 10):
                if worksheet.cell(i, j).value != '':
                    master_num = worksheet.cell(i, 0).value
                    master_key.append(worksheet.cell(0, j).value)
                    master_value.append(worksheet.cell(i, j).value)
            # slave药物的有效信息是25，最后一列
            for k in range(25, columns):
                if worksheet.cell(i, k).value != '':
                    slave_num = worksheet.cell(i, 23).value
                    slave_key.append(worksheet.cell(0, k).value)
                    slave_value.append(worksheet.cell(i, k).value)
            # 对两类药物分别打包成字典
            master = dict(zip(master_key, master_value))
            slave = dict(zip(slave_key, slave_value))
            # 再对两类药物进行封装，加上num参数，方便后面的数据库操作
            master_c = Drug(master, master_num)
            slave_c = Drug(slave, slave_num)
            # 第一次初始化经过这里
            if data["master"] == {}:
                print 'data["master"] == {}', worksheet.cell(i, 23).value
                data["master"] = master_c
                data["slave"].append(slave_c)
                continue
            # 若master相同，则将slave加入尾部，即master对应行没有num
            if worksheet.cell(i, 0).value == '':
                print 'master num is empty', worksheet.cell(i, 23).value
                data["slave"].append(slave_c)
            # 若master行有num，即说明是到了下一个master，此时将上一次的data存入，初始化新的data
            if worksheet.cell(i, 0).value != '':
                print 'current master num:%s, previous master num:%s ' % (worksheet.cell(i, 0).value, data["master"].num)
                print "new one ", worksheet.cell(i, 23).value
                package.append(data)
                data = {"master": {}, "slave": []}
                data["master"] = master_c
                data["slave"].append(slave_c)
        print "\n"
    # 由于每次都是存上次的data，导致最后循环做完的时候最后一个data没有被插入，这里插入
    package.append(data)
    print 'length:', len(package)
    for each in package:
        print 'master:', each["master"].num
        for each_slave in each["slave"]:
            print each_slave.num
            slaveinfo = each_slave.info
            for i in slaveinfo:
                print "%s %s" % (i, slaveinfo[i])
    return package
if __name__ == '__main__':
    value = "./59146.xls"
    openxl(value)
