import xlwt
import os


def detector_export(ret_dic):
    folder_path = os.path.split(os.path.abspath(__file__))[0]
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('隐私数据分布')
    title = ['文件', '身份证号', '手机号', '银行卡号', '固定电话', '家庭地址']
    i = 0
    col = 0
    for header in title:
        sheet.write(0, i, header)
        i += 1
    row = 1
    for k in ret_dic:
        sheet.write(row, 0, k)
        sheet.write(row, 1, ret_dic[k]['id_card'])
        sheet.write(row, 2, ret_dic[k]['cellphone'])
        sheet.write(row, 3, ret_dic[k]['bank_card'])
        sheet.write(row, 4, ret_dic[k]['fix_line'])
        sheet.write(row, 5, ret_dic[k]['addr'])
        row += 1

    export_path = folder_path + r"\隐私鉴别结果.xls"
    book.save(export_path)
    print("结果导出成功")
