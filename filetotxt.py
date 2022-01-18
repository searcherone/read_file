"""
 author: lijingcan
 datetime: 2021/10/28
 coding: utf-8
 project name: file_traversal
 Program function: 抽取word文档文本内容转换成txt格式
"""

"""
功能描述：文件转存txt，保存在指定目录中
参数描述：1、filePath：文件路径；2、savePath：保存路径
"""
"""
实现步骤：
    # 1、切分文件路径为文件目录和文件名
    # 2、修改切分后的文件后缀
    # 3、设置新的文件保存路径
    # 4、加载文本提取的处理程序
    # 5、保存文本信息
"""
# coding=utf-8
import os  # 路径
import fnmatch  # 后缀名的一个包
import time
import pathlib
import pandas as pd
from pdfminer import high_level
from win32com import client as wc
from win32com.client import Dispatch, DispatchEx


def word2txt(filepath, savepath=''):
    # 1、切分文件路径为文件目录和文件名
    try:
        dirs, filename = os.path.split(filepath)
        filename_extension, extension = os.path.splitext(filename)
        new_name = filename_extension + str(int(time.time()*1000000)) + '.txt'
        # 3、设置新的文件保存路径
        if savepath == '':
            savepath = dirs  # 保存到原始路径
        else:
            savepath = savepath  # 传递的路径
        word2txtpath = os.path.join(savepath, new_name)  # 连接
        print('新的文件绝对路径 = ', word2txtpath)
        # 4、加载文本提取的处理程序，word->txt
        wordapp = wc.Dispatch('Word.Application')  # 启动应用程序
        # wordapp.Visible = True
        # wordapp.DisplayAlerts = 0
        mytxt = wordapp.Documents.Open(filepath)  # 打开文件路径

        # 5、保存文本信息
        mytxt.SaveAs(word2txtpath, 4)  # 以txt格式保存，参数4代表抽取文本
        mytxt.Close()
        return new_name
        # wordapp.Quit()
    except Exception as e:
        print("%s转txt报错信息: %s " % (filepath, e))
        return "转换错误"


def pdf2txt(filepath, savepath = ''):
    try:
        # 1、切分文件路径为文件目录和文件名
        dirs, filename = os.path.split(filepath)
        filename_extension, extension = os.path.splitext(filename)
        new_name = filename_extension + str(int(time.time()*1000000)) + '.txt'
        # 2、设置新的文件保存路径
        if savepath == '':
            savepath = dirs
        else:
            savepath = savepath
        pdf2txtpath = os.path.join(savepath, new_name)
        print('新的文件绝对路径=', pdf2txtpath)

        # 4、加载文本提取的处理程序，pdf->txt
        text = high_level.extract_text(filepath)
        content = ""
        pathlib.Path(pdf2txtpath).touch()
        fp = open(pdf2txtpath, 'rb+')
        fp.write(text.encode(encoding='UTF-8', errors='strict'))
        fp.write(b'\n')
        fp.close()
        return new_name
    except Exception as e:
        print("%s转txt报错信息: %s " % (filepath, e))
        return "转换错误"


def excel2txt(filepath, savepath = ''):
    try:
        # 1、切分文件路径为文件目录和文件名
        dirs, filename = os.path.split(filepath)
        filename_extension, extension = os.path.splitext(filename)
        # print('原始文件路径：', dirs)
        # print('原始文件名：', filename)
        new_name = filename_extension + str(int(time.time() * 1000000)) + '.txt'
        # 2、设置新的文件保存路径
        if savepath == '':
            savepath = dirs
        else:
            savepath = savepath
        pdf2txtpath = os.path.join(savepath, new_name)
        print('新的文件绝对路径=', pdf2txtpath)
        df = pd.read_excel(filepath, sheet_name=None)
        # pathlib.Path(pdf2txtpath).touch()
        # df['IDEA插件需求'].to_csv(pdf2txtpath, encoding='UTF-8', sep=',', index=False)
        for key in df.keys():
            df[key].to_csv(pdf2txtpath, encoding='UTF-8', sep=',',  mode='a', index=False)
        return new_name
    except Exception as e:
        print("%s转txt报错信息: %s " % (filepath, e))
        return "转换错误"

# if __name__ == '__main__':
#     filepath = r'C:\Users\94417\Documents\WeChat Files\wxid_hzaaw2yvlb7c22\FileStorage\File\2021-08\发票邮件特殊词汇黑白名单.xls'
#     savepath = r'D:\file_traversal'
#     ret = excel2txt(filepath, savepath)  # 函数实例化
#     if ret != "转换错误":
#         new_name = ret
#     print('word信息抽取到txt格式中完成')
