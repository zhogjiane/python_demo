# python_demo


~~~
import configparser
import io
import json
import logging
from threading import Timer
import socket

import nacos
import numpy as np
import pandas as pd
from flask import Flask, Response, make_response, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
host_name = socket.gethostname()
host = socket.gethostbyname(host_name)


SEQ_LENGTH = 100
SERVER_ADDRESSES = "dev.nacos.icpx.hoteamsoft.com:30848"
NAMESPACE = "slide-dev"
client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE)
nacos_conf = client.get_config("icp-cloud-bda-pre-charging-circuitfault-detection-service-develop", "DEFAULT_GROUP", True,
                               True)
conf = configparser.ConfigParser()
conf.readfp(io.StringIO(nacos_conf))

clientInstance = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, username="icpx-dev", password="icpx-dev@icpx2021")


clientInstance.add_naming_instance("icp-cloud-bda-pre-charging-circuitfault-detection-service-develop", conf.get("app", "host"),
                                   conf.get("flask", "port"), "DEFAULT")


def heartbeatCheck():
    try:
        clientInstance.send_heartbeat("icp-cloud-bda-pre-charging-circuitfault-detection-service-develop",conf.get("app", "host"),
                                    conf.get("flask", "port"), "DEFAULT")
    except Exception as e:
        logging.error('Reason:', e)


class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


t = RepeatingTimer(3.0, heartbeatCheck)
t.start()


@app.route("/info", methods=["GET"])
def info():
    return "Sucess"


@app.route("/health", methods=["GET"])
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype='application/json')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def str_to_bool(string):
    return True if string.lower() == 'true' else False


def Kv(arr):
    # arr.shape = (m, n)
    # return: Kv.shape = (1, n)

    arr = np.array(arr)

    # 计算峭度
    rms = arr ** 2
    rms = rms.mean()
    rms = rms ** 2

    K = arr ** 4
    K = K.mean()

    Kv = K / rms
    return Kv


def CH1():
    CH1Result = list()
    # 预充电接触器线圈电压(CH1)
    for num in range(1, 11):
        data_path = "data/tek_data" + str(num) + ".csv"
        df = pd.read_csv(data_path)
        s = df["1"]

        #     start = np.argwhere(s>0.01)[0][0] - 500
        #     interval = 3000
        #     data = np.array(s[start:start+interval])
        CH1Result.append(Kv(s))
    return CH1Result


def CH2():
    CH2Result = list()
    # 预充电接触器线圈电流(CH2)
    for num in range(1, 11):
        data_path = "data/tek_data" + str(num) + ".csv"
        df = pd.read_csv(data_path)
        s = df["2"]

        #     start = np.argwhere(s>0.01)[0][0] - 500
        #     interval = 3000
        #     data = np.array(s[start:start+interval])
        CH2Result.append(Kv(s))
    return CH2Result


def CH4():
    CH4Result = list()
    # 主接触器线圈电压(CH4)
    for num in range(1, 11):
        data_path = "data/tek_data" + str(num) + ".csv"
        df = pd.read_csv(data_path)
        s = df["4"]

        #     start = np.argwhere(s>0.01)[0][0] - 500
        #     interval = 3000
        #     data = np.array(s[start:start+interval])
        CH4Result.append(Kv(s))
    return CH4Result


def CH5():
    CH5Result = list()
    # 主接触器线圈电流(CH5)
    for num in range(1, 11):
        data_path = "data/tek_data" + str(num) + ".csv"
        df = pd.read_csv(data_path)
        s = df["5"]

        #     start = np.argwhere(s>0.01)[0][0] - 500
        #     interval = 3000
        #     data = np.array(s[start:start+interval])
        CH5Result.append(Kv(s))
    return CH5Result


def CH7():
    CH7Result = list()
    # 预充电电压(CH7)
    for num in range(1, 11):
        data_path = "data/tek_data" + str(num) + ".csv"
        df = pd.read_csv(data_path)
        s = df["7"]

        #     start = np.argwhere(s>0.01)[0][0] - 500
        #     interval = 3000
        #     data = np.array(s[start:start+interval])
        CH7Result.append(Kv(s))
    return CH7Result


def CH8():
    CH8Result = list()
    # 预充电电流(CH8)
    for num in range(1, 11):
        data_path = "data/tek_data" + str(num) + ".csv"
        df = pd.read_csv(data_path)
        s = df["8"]

        #     start = np.argwhere(s>0.01)[0][0] - 500
        #     interval = 3000
        #     data = np.array(s[start:start+interval])
        CH8Result.append(Kv(s))
    return CH8Result


class ModelRun(Resource):

    @classmethod
    def post(cls):
        result = {'chone': CH1(), 'chtwo': CH2(), 'chfour': CH4(), 'chfive': CH5(), 'chseven': CH7(), 'cheight': CH8()}
        return Response(json.dumps(result), mimetype='application/json')


# flask添加资源和资源标识
api.add_resource(ModelRun, '/precharging/v1/predict')

if __name__ == '__main__':
    app.run(debug=str_to_bool(conf.get("flask", "debug")), port=int(conf.get("flask", "port")),
            host=conf.get("flask", "host"))

