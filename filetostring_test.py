import time

import filetostring

start_time = time.time()
content = filetostring.read_pdf(r'C:\Users\94417\Desktop\内容安全鉴别系统\个人隐私\测试样例\pdf\createpdf敏感_1_30.pdf')
print(len(content))
print(content[0:2000])
end_time = time.time()
print(content[-1000:])
print("程序时间:", end_time-start_time)
