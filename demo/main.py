from flask import Flask, request, flash, render_template, redirect, url_for
from sql_func import *
from flask_cors import CORS
from flask_login import UserMixin, LoginManager, login_required, logout_user, login_user, current_user

app = Flask(__name__)
CORS(app, resources=r'/*')

app.secret_key='abc'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied.'

login_manager.init_app(app)  # 初始化应用

class UserService:
    users = [
        {'id': 1, 'username': 'root', 'password': '111111'},
        {'id': 2, 'username': 'custom', 'password': '2222222'}
    ]

    @classmethod
    def query_user_by_name(cls, username):
        for user in cls.users:
            if username == user['username']:
                return user

    @classmethod
    def query_user_by_id(cls, user_id):
        for user in cls.users:
            if user_id == user['id']:
                return user

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(user_id: str):
    if UserService.query_user_by_id(int(user_id)) is not None:
        curr_user = User()
        curr_user.id = user_id
        return curr_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        username = request.form.get('username')
        user = UserService.query_user_by_name(username)

        if user is not None and request.form['password'] == user['password']:
            curr_user = User()
            curr_user.id = user['id']

            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)

            # 登录成功后重定向
            return redirect(url_for('index'))
        error = 'Wrong username or password!'
    return render_template('login.html', error=error)


@app.route('/', methods=['Get', 'Post'])
@login_required
def index():
    return render_template('index.html')


@app.route('/addFlight/', methods=['Get', 'Post'])
def addFlight():
    form = request.form
    companycode = form['company-code-add']
    departcode = form['depart-code-add']
    arrivecode = form['arrive-code-add']
    linecode = form['line-code-add']
    result = add_flight(companycode, departcode, arrivecode, linecode)
    if result == "ok":
        return "执行成功"
    else:
        return result


@app.route('/delFlight/', methods=['Get', 'Post'])
def deleteFlights():
    form = request.form
    delcode = form['line-code-del']
    result = delete_flight(delcode)
    if result == "ok":
        return "执行成功"
    else:
        return result


@app.route('/flightModify/', methods=['Get', 'Post'])
def flightModify():
    form = request.form
    print(form)
    linecode = form['line_code_modify']
    departdate = form['depart_code_modify'].replace('/', '')
    flytime = form['flytime_modify']
    arrtime = form['arrive_time_modify']
    eco = form['eco']
    ecoPrice = form['ecoPrice']
    lux = form['lux']
    luxPrice = form['luxPrice']
    status = form['status']
    result = add_timetable(linecode, departdate, flytime, arrtime, eco, lux, ecoPrice, luxPrice, status)
    if result == "ok":
        return "执行成功"
    else:
        return result

@app.route('/selectFlight/', methods=['Get', 'Post'])
def SelectTickets():
    form = request.form
    departdate = form['depart_date_select'].replace('/', '')
    departcode = form['depart-loc-select']
    arrcode = form['line-loc-select']
    result = select_flights(departdate, departcode, arrcode)
    return result

@app.route('/AddCN/', methods=['Get', 'Post'])
def Add_CN():
    form = request.form
    print(form)
    nation = "中国"
    name = form['name']
    name_pinyin = form['name_pinyin']
    minzu = form['minzu']
    sfz = form['sfz']
    phone = form['phone']
    sex = form['sex']
    result = add_CN(name_pinyin, name, nation, phone, sfz, minzu, sex)
    if result == "ok":
        return "执行成功"
    else:
        return result

@app.route('/AddFR/', methods=['Get', 'Post'])
def Add_FR():
    form = request.form
    nation = form['nation2']
    name = form['en']
    passport = form['passport']
    visa = form['visa']
    phone = form['phone']
    sex = form['sex']
    result = add_FR(name, nation, phone, passport, visa, sex)
    if result == "ok":
        return "执行成功"
    else:
        return result


@app.route('/BuyTickets/', methods=['Get', 'Post'])
def BuyTickets():
    form = request.form
    print(form)
    linecode = form['line-code']
    departdate = form['date_buy'].replace('/', '')
    sfz = form['sfz']
    seat = form['seat']
    result = buy(linecode, departdate, sfz, seat)
    if result == "ok":
        return "购票成功"
    else:
        return result

@app.route('/ticketBack/', methods=['Get', 'Post'])
def ticketBack():
    form = request.form
    linecode = form['line-code']
    departdate = form['date_buy'].replace('/', '')
    sfz = form['sfz']
    seat = form['seat']
    result = ticket_back(linecode, departdate, sfz, seat)
    if result == "ok":
        return "退票成功"
    else:
        return result

@app.route('/delbanci/', methods=['Get', 'Post'])
def delBanci():
    form = request.form
    linecode = form['line_code']
    departdate = form['depart_date_banci'].replace('/', '')
    result = del_banci(linecode, departdate)
    if result == "ok":
        return "班次删除成功"
    else:
        return result

@app.route('/bookticket/', methods=['Get', 'Post'])
def bookticket():
    form = request.form
    departdate = form['book_date'].replace('/', '')
    linecode= form['book_code']
    result = book_ticket(departdate, linecode)
    return result


if __name__ == '__main__':
    app.run()
