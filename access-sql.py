#%%
import pypyodbc
import pandas as pd
from datetime import datetime as t
#定义conn
def mdb_conn(db_name, password = ""):
    """
    功能：创建数据库连接
    :param db_name: 数据库名称
    :param db_name: 数据库密码，默认为空
    :return: 返回数据库连接
    """
    str = 'Driver={Microsoft Access Driver (*.mdb)};PWD' + password + ";DBQ=" + db_name
    conn = pypyodbc.win_connect_mdb(str)

    return conn

def mdb_sel(cur, sql):
    """
    功能：向数据库查询数据
    :param cur: 游标
    :param sql: sql语句
    :return: 查询结果集
    """
    try:
        cur.execute(sql)
        return cur.fetchall()
    except:
        return []

pathfile = input('文件名:')
sql = input('查询语句:')
s=t.now()

conn = mdb_conn(pathfile)
cur = conn.cursor()
#查

sel_data = mdb_sel(cur, sql)
df=pd.DataFrame(sel_data)
df.to_excel(r'\\Nas\信息开发部\信息部\out\导出数据.xlsx',index=False)

cur.close()    #关闭游标
conn.close()   #关闭数据库连接
e=t.now()
print(e-s)

# %%
