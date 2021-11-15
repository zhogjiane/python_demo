#引入flask，读取配置
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#flask 读取config文件中的配置信息
app.config.from_object('config')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/flask_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, email=form.name.data + '@example.com')
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


# 反向解析URl
@app.route('/userjsjsjjajjkshdaskjhdajkshd'， methods=['GET', 'POST']，endpoint='user')
var url = url_for('user', username='john', _external=True)
print(url)


# python mysql操作
import pymysql


conn = pymysql.connect(host='localhost', user='root', password='123456', db='flask_test', charset='utf8')
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()


# flask-sqlalchemy操作
from flask_sqlalchemy import SQLAlchemy

#  python 使用静态方法 mysql操作
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@staticmethod
def mysql_connect():
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/flask_test')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

@staticmethod
def mysql_insert(session, user):
    session.add(user)
    session.commit()

@staticmethod
def mysql_delete(session, user):
    session.delete(user)
    session.commit()

@staticmethod
def mysql_update(session, user):
    session.add(user)
    session.commit()

@staticmethod
def mysql_select(session, user):
    return session.query(user)

@staticmethod
def mysql_select_one(session, user):
    return session.query(user).first()

@staticmethod
def mysql_select_all(session, user):
    return session.query(user).all()

@staticmethod
def mysql_select_filter(session, user, **kwargs):
    return session.query(user).filter_by(**kwargs)

@staticmethod
def close(conn, cursor):
    cursor.close()
    conn.close()




# python 数据库连接池
import pymysql

@staticmethod
def mysql_connect():
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='flask_test', charset='utf8')
    return conn

@staticmethod
def open_mysql_connect():
    conn = mysql_connect()
    cursor = conn.cursor()
    return conn, cursor

@staticmethod
def close_mysql_connect(conn, cursor):
    cursor.close()
    conn.close()

@staticmethod
.pool from  Pool
def open_mysql_connect():
    conn = Pool.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor



if __name__ == '__main__':
    app.run(debug=True)
    




# 安装Flask-WTF
# pip install Flask-WTF
# 安装WTForms
# pip install WTForms
# 安装Flask-SQLAlchemy
# pip install Flask-SQLAlchemy
# 安装Flask-Script
# pip install Flask-Script
# 安装Flask-Migrate
# pip install Flask-Migrate
