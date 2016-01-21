# encoding:utf-8
import MySQLdb
import sys
import os
reload(sys)
exec("sys.setdefaultencoding('utf-8')")


def init_database(host, username, password, database):
    conn = MySQLdb.connect(host, username, password, database)
    cur = conn.cursor()
    # print("连接数据库%s成功！") % database
    cur.execute("SET NAMES utf8")
    conn.commit()
    return cur, conn


def close(cur, conn):
    cur.close()
    conn.close()
    # print "关闭连接！"

if __name__ == "__main__":
    cur, conn = init_database()
    # sql = "insert into drug_mapper (target,matched) values(1,1)"
    sql = "select * from drug_mapper;"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    # print u"关闭连接！"
