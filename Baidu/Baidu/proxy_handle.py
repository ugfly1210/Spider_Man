# 1、与middlewares.py同级目录下新建proxy_handle.py
import requests


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").text


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


