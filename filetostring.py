"""
 author: lijingcan
 datetime: 2022/01/19
 coding: utf-8
 project name: read_file
 Program function: 读取docx、csv、xlsx、xls、pdf中的文本内容
"""

"""
功能描述：读取常见文件的文本内容
参数描述：filePath：文件路径；
"""

import csv
# coding=utf-8
import os

import docx
import xlrd
from pdfminer import high_level


def read_file(filepath):
    _, extension = os.path.splitext(filepath)
    content = ""
    if extension == ".xls" or extension == ".xlsx":
        content = read_excel(filepath)
    if extension == ".csv":
        content = read_csv(filepath)
    elif extension == ".txt":
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:  # 打开文件
            content = f.read()  # 读取文件
        f.close()
    elif extension == ".docx":
        content = read_docx(filepath)
    elif extension == ".pdf":
        content = read_pdf(filepath)
    return content


def read_docx(filepath):
    # 用docx包读取docx文件
    content = ""
    file = docx.Document(filepath)
    for para in file.paragraphs:
        content += para.text
    return content


def read_pdf(filepath):
    # 用pdfminer中的high_level包读取PDF文件的文本
    content = high_level.extract_text(filepath)
    return content


def read_excel(filepath):
    # 用pandas包读取excel文件
    content = ""
    workbook = xlrd.open_workbook(filepath)
    for sheet in workbook.sheets():
        row_number = sheet.nrows
        for i in range(row_number):
            column_number = len(sheet.row(i))
            for j in range(column_number):
                content += sheet.cell_value(i, j) + ','
    return content


def read_csv(filepath):
    # 用csv包读取csv文件
    content = ""
    csv_file = csv.reader(open(filepath, 'r'))
    for row in csv_file:
        for i in range(len(row)):
            content += row[i] + ','
    return content
# if __name__ == '__main__':
#     filepath = r'C:\Users\94417\Documents\WeChat Files\wxid_hzaaw2yvlb7c22\FileStorage\File\2021-08\发票邮件特殊词汇黑白名单.xls'
#     savepath = r'D:\file_traversal'
#     ret = excel2txt(filepath, savepath)  # 函数实例化
#     if ret != "转换错误":
#         new_name = ret
#     print('word信息抽取到txt格式中完成')
