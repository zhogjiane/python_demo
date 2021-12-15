<<<<<<< HEAD

#flask 读取config文件中的配置信息
app.config.from_object('config')



@app.route('/', methods=['GET', 'POST'])


# 反向解析URl
@app.route('/userjsjsjjajjkshdaskjhdajkshd'， methods=['GET', 'POST']，endpoint='user')
var url = url_for('user', username='john', _external=True)
print(url)

@staticmethod
def mysql_connect():
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/flask_test')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

# python 数据库连接池
@staticmethod
def mysql_connect():
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='flask_test', charset='utf8')
    return conn
=======
# 引入flask框架
from flask import Flask,jsonify,request
import json
from flask.wrappers import Response
# 引入myql驱动
import pymysql
# 引入pandas
import pandas as pd

app = Flask(__name__)
>>>>>>> 0afc700c5cead178311382037713d399162e4835


#  定义一个接口操作数据库
@app.route('/run3',methods=['GET','POST'])
def run3():
    if request.method == 'POST':
        # 获取前端传递的参数 使用json.loads()方法将json字符串转换为python对象 
        # data = json.loads(request.get_data())
        # 获取数据库连接
        engine = pymysql.connect(host='localhost',user='root',password='123456',database='pythondatabase',port=3309,charset='utf8')
        # 获取游标
        cursor = engine.cursor()        
        # 获取'C2'那一列的值的sql语句
        sql2c2 = "select C2 from tek_data1"
        # cursor执行语句
        cursor.execute(sql2c2)
        # 返回json结果，并只显示了value的值。
        # result=pd.read_sql_query(sql2c2,engine)['C2'].to_json(orient='values')
        # 返回list形式的数据
        result = pd.read_sql_query(sql2c2,engine)['C2'].to_list()
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        engine.close()
        # 返回结果
        return Response(json.dumps(result),mimetype='application/json')

<<<<<<< HEAD
@staticmethod

def open_mysql_connect():
    conn = Pool.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor


# 增加一个post接口 /api/v1/contacts 接受参数
app.route("/api/v1/contacts", methods=["POST"])
def add_contact():
    contact = request.json
    contact_id = model.add_contact(contact)
    return jsonify({'contact_id': contact_id})


=======





if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 0afc700c5cead178311382037713d399162e4835