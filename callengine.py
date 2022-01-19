# coding=utf-8
import json

import requests


def engine_call(url, file_path, content):
    s = json.dumps({'file_name': file_path, 'content': content})
    try:
        ret = requests.post(url, data=s)
    except requests.exceptions.ConnectionError as e:
        print("http连接错误，报错信息: %s" % e)
        return ""
    ret = json.loads(ret.text)
    return ret
