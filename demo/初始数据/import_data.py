import pymysql
import pandas as pd

# 打开数据所在的路径表名
# data = pd.read_excel('航空公司代码表.xlsx')
data = pd.read_excel('机场代码表.xlsx')

# 这个是表里的sheet名称（注意大小写）


# 建立一个 MySQL连接
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="020127",
    database="Flight_Sys",
    charset="utf8mb4"
)

# 获得游标
cur = conn.cursor()

# 创建插入sql语句
query = 'insert into airport(airportno,airportname)values(%s,%s)'
# query = 'insert into airline(code,airlinename)values(%s,%s)'
# 创建一个for循环迭代读取xls文件每行数据的，
# 从第二行开始是要跳过标题行
# 括号里面1表示从第二行开始(计算机是从0开始数)
for i in range(0, len(data)):
    # (r, 0)表示第二行的0就是表里的A1:A1
    id = data.iloc[i][1]
    name = data.iloc[i][0]
    values = (id, name)
    # 执行sql语句
    cur.execute(query, values)

# close关闭文档
cur.close()
# commit 提交
conn.commit()
conn.close()


data = pd.read_excel('航空公司代码表.xlsx')
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="020127",
    database="Flight_Sys",
    charset="utf8mb4"
)
# 获得游标
cur = conn.cursor()

query = 'insert into airline(code,airlinename)values(%s,%s)'
# 创建一个for循环迭代读取xls文件每行数据的，
# 从第二行开始是要跳过标题行
# 括号里面1表示从第二行开始(计算机是从0开始数)
for i in range(0, len(data)):
    # (r, 0)表示第二行的0就是表里的A1:A1
    id = data.iloc[i][1]
    name = data.iloc[i][0]
    values = (id, name)
    # 执行sql语句
    cur.execute(query, values)

# close关闭文档
cur.close()
# commit 提交
conn.commit()

# 关闭MySQL链接
conn.close()
