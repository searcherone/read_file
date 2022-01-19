import argparse
import time
import os
import sys
import exportresult
import callengine
import filetostring
import findfile


def main():
    parser = argparse.ArgumentParser(description='隐私鉴别所需参数')
    parser.add_argument('-p', '--path', type=str, default=r'D:\测试样例', help='指定鉴别目录，默认为D:\\测试样例')
    parser.add_argument('-i', '--interface', type=str, default='detector', help='调用接口，detector返回简洁结果，\
                        detail返回详细结果，默认为detector')
    args = parser.parse_args()
    path = args.path
    if not os.path.isdir(path):
        sys.exit("指定目录不存在")
    inter = args.interface
    ret_dic = {}
    file_list = findfile.find_path(path)
    url = r"http://127.0.0.1:12445/" + inter
    for file_path in file_list:
        content = filetostring.read_file(file_path)
        if content:
            ret = callengine.engine_call(url, file_path, content)
        if not ret:
            print("个人隐私鉴别引擎端口异常")
            break
        else:
            print("%s文件的鉴别结果: %s" % (file_path, ret))
            if ret['msg'] == 'succ':
                ret_dic[file_path] = ret['data']
    exportresult.detector_export(ret_dic)


if __name__ == '__main__':
    time_start = time.time()
    main()
    time_end = time.time()
    print('程序总耗时=', time_end - time_start)
