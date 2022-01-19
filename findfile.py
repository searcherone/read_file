"""
单线程版本，249秒
#environment:   python 3.7.6 + Windows
#author:        lijingcan
#time:          2022年01月19日09:27
#work:          扫描指定目录下所有后缀为docx、csv、xlsx、xls、pdf、txt的文件
"""
# coding=utf-8
import os


# 全局变量
# 此处用来写入需要查找的文件后缀，例如'.doc', '.docx'
search_file = {'.docx': True,  '.xlsx': True, '.xls': True, '.csv': True, '.pdf': True, '.txt': True}
file_list = []


def error_waring():
    pass


# 遍历目录、找出文件
def find_path(path):
    for root, dirs, files in os.walk(path, topdown=True, onerror=error_waring()):
        for filename in files:
            filename_extension, extension = os.path.splitext(filename)
            if extension in search_file:
                file_path = os.path.join(root, filename)
                file_list.append(file_path)
    print("文件遍历成功，共%d个可解析文件" % len(file_list))
    return file_list


