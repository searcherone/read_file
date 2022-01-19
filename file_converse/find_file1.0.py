"""
单线程版本，380秒
#environment:   python 3.7.6 + Windows
#author:        lijingcan
#time:          2021年10月27日15:00:00
#work:          扫描磁盘下的所有.doc, .docx, .txt, .ppt, .xsl, .csv, .ppt输出到指定文件
#使用前请先安装psutil库、 pip install psutill
# 模块
"""
# coding=utf-8
import os
import pathlib
import re
import time

import psutil

"""
#print(os.popen("wmic volume get lable, name").read())
# 获取磁盘、不适用于Windows10
#打开一个管道，它通往 / 接受自命令 cmd。返回值是连接到管道的文件对象，根据 mode 是 'r' （默认）还是 'w' 决定该对象可以读取还是写入。
"""
# 全局变量
# 此处用来写入需要查找的文件后缀，例如'.doc', '.docx'
search_file = ['.docx', '.doc', '.xlsx', '.xls', '.csv', 'pdf', '.ppt', '.pptx', '.7z', '.rar', '.zip', '.txt']
# result_file = 'c:/administrator/desktop/abc.txt'
result_file = r'C:\Users\94417\Desktop\result.txt'                 # 此处写入输出文件的位置
file_list = []
disks = []  # 用来存放磁盘


# 错误提示
def error_waring():
    pass


def check():
    if not result_file:
        print('您还没有填入保存结果的文件路径--result_file')
        print('程序已默认为您选择保存路径，桌面/result.txt')
    if not search_file:
        print('您还没有填入需要查找的文件后缀--search_file')
        quit()


# 获取本地磁盘
def find_disk():
    disk = str(psutil.disk_partitions())
    for j in re.finditer('device', disk):
        start = j.span()[1]+2
        end = j.span()[1] + 4
        disks.append(disk[start:end]+'\\')
        # in_queue.put(disk[start:end]+'\\')


def find_path(path):
    # path = iq.get()
    # 遍历磁盘、找出文件
    for root, dirs, files in os.walk(path, topdown=True, onerror=error_waring()):
        for filename in files:
            filename_extension, extension = os.path.splitext(filename)
            if extension in search_file:
                file_path = os.path.join(root, filename)
                file_list.append(file_path)
                print("文件路径: %s" % (file_path))


# 主函数 ==》 从C盘开始寻找，依次遍历
if __name__ == '__main__':
    time_start = time.time()
    pathlib.Path(result_file).touch()
    print('程序运行中...')
    check()
    find_disk()
    for i in disks:
        find_path(i)
    fp = open(result_file, 'rb+')
    for file_p in file_list:
        fp.write(file_p.encode(encoding='UTF-8', errors='strict'))
        fp.write(b'\n')
    fp.close()
    time_end = time.time()
    print('程序总耗时=', time_end - time_start)
