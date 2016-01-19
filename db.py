# encoding:utf-8
import MySQLdb
import sys
import os
reload(sys)
exec("sys.setdefaultencoding('utf-8')")


def init_database(host, username, password, database):
    conn = MySQLdb.connect(host, username, password, database)
    cur = conn.cursor()
    print u"连接数据库成功！"
    cur.execute("SET NAMES utf8")
    conn.commit()
    return cur, conn

    if __name__ == "__main__":
        cur, conn = init_database()
        # sql = "insert into drug_mapper (target,matched) values(1,1)"
        sql = "select * from drug_mapper;"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print u"关闭连接！"
