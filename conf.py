import nacos
import configparser
import io
import logging
# 引入线程模块 模拟nacos心跳监测
from threading import Timer

SERVER_ADDRESSES = "10.0.59.135:30848"
NAMESPACE = "slide-dev"
client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE)
nacos_conf = client.get_config("fuwuming", "DEFAULT_GROUP", True,
                               True)
conf = configparser.ConfigParser()
conf.readfp(io.StringIO(nacos_conf))
clientInstance = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, username="username", password="password")
clientInstance.add_naming_instance("fuwuming", conf.get("app", "host"),
                                   conf.get("flask", "port"), "DEFAULT")

def heartbeatCheck():
    try:
        clientInstance.send_heartbeat("fuwuming", conf.get("app", "host"),
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