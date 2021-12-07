# 引入flask框架
from flask import Flask,jsonify,request
import json

app = Flask(__name__)


# 定义一个接口
@app.route('/run',methods=['GET','POST'])
def run():
    if request.method == 'POST':
        # 获取前端传递的参数 使用json.loads()方法将json字符串转换为python对象 
        global keywords_fangfa
        global yuliaoku
        global key_number
        global usde_hmpgid
        data = json.loads(request.get_data(as_text=True).encode('utf-8'))
        keywords_fangfa = data['keywords_fangfa']
        yuliaoku = data['yuliaoku']
        key_number = data['key_number']
        usde_hmpgid = data['usde_hmpgid']
        # 调用方法
    try:
        state_begin()
        Score().show_res()
        # stata_end('已完成')
        result = {'state': 'success'}
        return Response(json.dumps(result), mimetype='application/json')
    except Exception as e:
        result = {'state': 'fail', 'msg': str(e)}
        return Response(json.dumps(result), mimetype='application/json')

# 定义一个接口
@app.route('/run2',methods=['GET','POST'])
def run2():
    if request.method == 'POST':
        # 传入一个数组，接受并进行排序
        data = request.get_json()['data']
        # 定义一个空列表
        result = []
        # 循环遍历数组
        for i in data:
            # 将数据添加到空列表中
            result.append(i)
        # 对列表进行排序
        result.sort()
        # 返回结果
        return jsonify({'result':result})




if __name__ == '__main__':
    app.run(debug=True)