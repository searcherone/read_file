# This is a sample Python script.

import os
import pathlib
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import filetotxt


def file_trav(savepath):
    # find_start_time = time.time()
    # dir_list = find_file.find_disk()
    # file_lists = []
    # for i in dir_list:
    #     file_list = find_file.find_path(i)
    #     file_lists.extend(file_list)
    # find_end_time = time.time()
    # print("遍历目录所用时间: ", find_end_time - find_start_time)
    file_lists = [r'D:\文档\求职\应届\光大银行\北京市2016家定点医疗机构名单.xls']
    parser_result = {}
    to_start_time = time.time()
    for i in range(len(file_lists)):
        single_start_time = time.time()
        file_size = os.path.getsize(file_lists[i])
        if file_size > 104857600:
            continue
        filename_extension, extension = os.path.splitext(file_lists[i])
        ret = ''
        if extension == '.doc':
            ret = filetotxt.word2txt(file_lists[i], save_path)
        elif extension == '.xls':
            ret = filetotxt.excel2txt(file_lists[i], save_path)
        # elif extension == '.pdf':
        #     ret = filetotxt.pdf2txt(file_lists[i], save_path)
        if ret == '转换错误':
            continue
        elif ret != '':
            parser_result[file_lists[i]] = []
            parser_result[file_lists[i]].append([ret])
        else:
            parser_result[file_lists[i]] = []
            continue
        single_end_time = time.time()
        print("%s转换所用时间: " % file_lists[i], single_end_time - single_start_time)
    to_end_time = time.time()
    print("文件转换所用时间: ", to_end_time - to_start_time)
    return parser_result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("test-----")
    save_path = r'D:\file_traversal'
    time_start = time.time()
    parser_result = file_trav(save_path)
    print(parser_result)
    result_file = r'C:\Users\94417\Desktop\result.txt'
    pathlib.Path(result_file).touch()
    fp = open(result_file, 'w+')
    for i, v in parser_result.items():
        fp.write(i + " : " + str(v))
        fp.write('\n')
    fp.close()
    time_end = time.time()
    print('程序总耗时=', time_end - time_start)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
