# coding=utf-8
import subprocess
import time
import json
import find_file
from collections import defaultdict
start_time = time.time()
engine_path = r'C:\Users\94417\Desktop\内容安全鉴别系统\个人隐私\engine.exe'
# file_dic = find_file.find_path()
file_dic = []
identify_result = {}
print("txt文件数目: ", len(file_dic['.txt']))
for i in range(len(file_dic['.txt']//10)):
    file_path = ""
    order = engine_path
    for j in range(10):
        order = order + ' ' + file_dic['.txt'][i+j]
        subp = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
        subp.wait(30)
        if subp.poll() == 0:
            origin_res = subp.communicate()[0].decode('utf-8')
            json_res = json.loads(origin_res)
            for key, value in json_res['data'].items():
                key = key.replace("\\\\", "\\")
                identify_result[key] = value
        else:
            print("失败")
        end_time = time.time()
        print("程序时间: ", end_time - start_time)
