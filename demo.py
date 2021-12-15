
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


