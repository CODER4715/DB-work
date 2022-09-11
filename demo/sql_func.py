import pymysql
import traceback
from flask import render_template


def add_flight(AirlineCode, DeptAirport, ArvAirport, FlightNo):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="020127",
        database="Flight_Sys",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "insert into flight(flightno,dept_airport,arv_airport,code) VALUES (%s, %s, %s,%s );"
    result = ''
    try:
        # 执行SQL语句
        cursor.execute(sql, [FlightNo, DeptAirport, ArvAirport, AirlineCode])
        # 提交事务
        conn.commit()

        result = 'ok'
    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        result = str(e)

    cursor.close()
    conn.close()
    return result

def delete_flight(FlightNo):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="020127",
        database="Flight_Sys",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "call delete_flight(%s);"
    try:
        cursor.execute(sql, FlightNo)
        # 运行成功，提交事务
        conn.commit()
        result = "ok"

    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        result = str(e)

    cursor.close()
    conn.close()
    return result


def add_timetable(FlightNo, DeptDate, DeptTime, ArvTime, eco, lux, ecoPrice, luxPrice, status):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="020127",
        database="Flight_Sys",
        charset="utf8mb4"
    )
    cursor = conn.cursor()

    sql = "call modify_timetable(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    result = ''
    try:
        # 执行SQL语句
        cursor.execute(sql, [FlightNo, DeptDate, DeptTime, ArvTime, status, eco, lux, ecoPrice, luxPrice])
        # 提交事务
        conn.commit()
        result = "ok"
    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        result = str(e)

    cursor.close()
    conn.close()
    return result

def select_flights(DeptDate, DeptAirport, ArvAirport):  # 查timetable
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="020127",
        database="Flight_Sys",
        charset="utf8mb4"
    )
    cursor = conn.cursor()

    sql = "select * from search_tickets where deptdate=%s and dept=%s and arv=%s;"
    try:
        cursor.execute(sql, [DeptDate, DeptAirport, ArvAirport])
        rs = cursor.fetchall()
        return render_template('select.html', rs=rs)  # 返回表格
    except Exception as e:
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        result = str(e)
        return result


def add_CN(EnName, CNName, Nationality, Tel, ID, Ethnic, sex):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="020127",
        database="Flight_Sys",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "call information_updating_cn(%s,%s,%s,%s,%s,%s,%s);"
    result = ''
    try:
        cursor.execute(sql, [EnName, CNName, Nationality, Tel, ID, Ethnic, sex])
        conn.commit()
        result = 'ok'
    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        result = str(e)
    cursor.close()
    conn.close()
    return result


def add_FR(EnName, Nationality, Tel, PassportNo, VisaNo, sex):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="020127",
        database="Flight_Sys",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "call information_updating_fr(%s,%s,%s,%s,%s,%s);"
    result = ''
    try:
        # 执行SQL语句
        cursor.execute(sql, [EnName, Nationality, Tel, PassportNo, VisaNo, sex])
        # 提交事务
        conn.commit()
        result = 'ok'
    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        result = str(e)

    cursor.close()
    conn.close()
    return result


def buy(FlightNo, DeptDate, ID_PassportNo, seat):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="020127",
        database="Flight_Sys",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "call buyT(%s,%s,%s,%s);"
    try:
        cursor.execute(sql, [FlightNo, DeptDate, ID_PassportNo, seat])
        conn.commit()
        result = 'ok'

    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        result = str(e)
    cursor.close()
    conn.close()
    return result

def ticket_back(FlightNo, DeptDate, ID_PassportNo, seat):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="020127",
        database="Flight_Sys",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "call ticket_back(%s,%s,%s,%s);"
    try:
        cursor.execute(sql, [FlightNo, DeptDate, ID_PassportNo, seat])
        conn.commit()
        result = 'ok'

    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        result = str(e)
    cursor.close()
    conn.close()
    return result

def del_banci(line_code, depart_date):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="020127",
        database="Flight_Sys",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "call del_banci(%s,%s);"
    try:
        cursor.execute(sql, [line_code, depart_date])
        conn.commit()
        result = 'ok'

    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        result = str(e)
    cursor.close()
    conn.close()
    return result

def book_ticket(DeptDate, linecode):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="020127",
        database="Flight_Sys",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "select * from book_tickets where deptdate=%s and flightno=%s;"
    try:
        cursor.execute(sql, [DeptDate, linecode])
        rs = cursor.fetchall()
        return render_template('ticket.html', rs=rs)  # 返回表格
    except Exception as e:
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        result = str(e)
        return result