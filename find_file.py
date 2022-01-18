"""
单线程版本，249秒
#environment:   python 3.7.6 + Windows
#author:        lijingcan
#time:          2021年10月27日15:00:00
#work:          扫描磁盘下的所有.doc, .docx, .txt, .ppt, .xsl, .csv, .ppt输出到指定文件
#使用前请先安装psutil库、 pip install psutill
# 模块
"""
# coding=utf-8
import os
import re
import time
import psutil
import pathlib
import collections
from threading import Thread
from queue import Queue
from collections import defaultdict

"""
#print(os.popen("wmic volume get lable, name").read())
# 获取磁盘、不适用于Windows10
#打开一个管道，它通往 / 接受自命令 cmd。返回值是连接到管道的文件对象，根据 mode 是 'r' （默认）还是 'w' 决定该对象可以读取还是写入。
"""
# 全局变量
# 此处用来写入需要查找的文件后缀，例如'.doc', '.docx'
search_file = {'.docx': True, '.doc': True, '.xlsx': True, '.xls': True, '.csv': True, '.pdf': True,
               '.ppt': True, '.pptx': True, '.7z': True, '.rar': True, '.zip': True, '.txt': True}
exclude_path = {'C:\\Windows': True, 'C:\\System Volume Information': True, 'C:\\ProgramData': True, 'C:\\Log': True,
                'C:\\Program Files (x86)': True, 'C:\\Program Files': True, 'C:\\Documents and Settings': True,
                'C:\\Intel': True, 'C:\\tmp': True, 'D:\\Program Files (x86)': True, 'D:\\Program Files': True,
                'D:\\ProgramData': True}
# result_file = 'c:/administrator/desktop/abc.txt'
file_dic = defaultdict(list)
file_list = []
dir_list = []  # 用来存放一级目录


# 错误提示
def error_waring():
    pass


# def check():
#     if not result_file:
#         print('您还没有填入保存结果的文件路径--result_file')
#         print('程序已默认为您选择保存路径，桌面/result.txt')
#     if not search_file:
#         print('您还没有填入需要查找的文件后缀--search_file')
#         quit()


# 获取本地的一级目录
def find_disk():
    disk = str(psutil.disk_partitions())
    for j in re.finditer('device', disk):
        start = j.span()[1]+2
        end = j.span()[1] + 4
        cha_disk = disk[start:end]+'\\'
        # in_queue.put(disk[start:end]+'\\')
        for root, dirs, files in os.walk(cha_disk, topdown=True, onerror=error_waring()):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                if dir_path not in exclude_path:
                    dir_list.append(dir_path)
            for file in files:
                filename_extension, extension = os.path.splitext(file)
                if extension in search_file:
                    file_list.append(os.path.join(root, file))
            break
    return dir_list


# 遍历磁盘、找出文件
def find_path(dir_list):
    for i in range(len(dir_list)):
        for root, dirs, files in os.walk(dir_list[i], topdown=True, onerror=error_waring()):
            for filename in files:
                filename_extension, extension = os.path.splitext(filename)
                if extension in search_file:
                    file_path = os.path.join(root, filename)
                    file_dic[extension].append(file_path)
                    print("文件路径: %s" % file_path)
    return file_dic

# 主函数 ==》 从C盘开始寻找，依次遍历
# if __name__ == '__main__':
#     time_start = time.time()
#     result_file = r'C:\Users\94417\Desktop\file_result.txt'  # 此处写入输出文件的位置
#     pathlib.Path(result_file).touch()
#     print('程序运行中...')
#     find_disk()
#     for i in dir_list:
#         start_time = time.time()
#         find_path(i)
#         end_time = time.time()
#         print("遍历%s目录所用时间: " % i, end_time-start_time)
#     fp = open(result_file, 'rb+')
#     for file_p in file_list:
#         fp.write(file_p.encode(encoding='UTF-8', errors='strict'))
#         fp.write(b'\n')
#     fp.close()
#     time_end = time.time()
#     print('程序总耗时=', time_end - time_start)
