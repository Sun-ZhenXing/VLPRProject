import MySQLdb
from MySQLdb import escape_string
from utils import host_name, user_name, passwd, db_name, charset

def esc_str(string):
    return str(escape_string(string), encoding='utf-8')


def get_version():
    db = MySQLdb.connect(host_name, user_name, passwd,
                         db_name, charset=charset)
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    db.close()
    return data[0]


def sql_exec(sql, feedback=False):
    """ 执行SQL语句并尝试返回数据 """
    results = None
    db = MySQLdb.connect(host_name, user_name, passwd,
                         db_name, charset=charset)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        if feedback:
            results = cursor.fetchall()
        else:
            db.commit()
    except:
        results = "ERROR"
        db.rollback()
    db.close()
    return results


if __name__ == "__main__":
    print(get_version())
    s = "-"
    if input("is feedback:") == "1":
        while s != "":
            s = input("> ")
            print(sql_exec(s, True))
    else:
        while s != "":
            s = input("> ")
            print(sql_exec(s))
