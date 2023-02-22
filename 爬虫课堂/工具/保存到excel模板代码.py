import os, xlwt, xlrd
from xlutils.copy import copy


def save_excel(data):
    # data = {
    #     '基本详情': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    # }
    os_path_1 = os.getcwd() + '/数据/'
    if not os.path.exists(os_path_1):
        os.mkdir(os_path_1)
    # os_path = os_path_1 + self.os_path_name + '.xls'
    os_path = os_path_1 + '数据.xls'
    if not os.path.exists(os_path):
        # 创建新的workbook（其实就是创建新的excel）
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建新的sheet表
        worksheet1 = workbook.add_sheet("基本详情", cell_overwrite_ok=True)
        borders = xlwt.Borders()  # Create Borders
        """定义边框实线"""
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40
        style = xlwt.XFStyle()  # Create Style
        style.borders = borders  # Add Borders to Style
        """居中写入设置"""
        al = xlwt.Alignment()
        al.horz = 0x02  # 水平居中
        al.vert = 0x01  # 垂直居中
        style.alignment = al
        # 合并 第0行到第0列 的 第0列到第13列
        '''基本详情13'''
        # worksheet1.write_merge(0, 0, 0, 13, '基本详情', style)
        excel_data_1 = ('评论内容', '评论时间', '点赞数', '用户名', '用户id', '用户性别', '用户地区',
                        '用户微博数', '用户粉丝数', '用户关注数')
        for i in range(0, len(excel_data_1)):
            worksheet1.col(i).width = 2560 * 3
            #               行，列，  内容，            样式
            worksheet1.write(0, i, excel_data_1[i], style)
        workbook.save(os_path)
    # 判断工作表是否存在
    if os.path.exists(os_path):
        # 打开工作薄
        workbook = xlrd.open_workbook(os_path)
        # 获取工作薄中所有表的个数
        sheets = workbook.sheet_names()
        for i in range(len(sheets)):
            for name in data.keys():
                worksheet = workbook.sheet_by_name(sheets[i])
                # 获取工作薄中所有表中的表名与数据名对比
                if worksheet.name == name:
                    # 获取表中已存在的行数
                    rows_old = worksheet.nrows
                    # 将xlrd对象拷贝转化为xlwt对象
                    new_workbook = copy(workbook)
                    # 获取转化后的工作薄中的第i张表
                    new_worksheet = new_workbook.get_sheet(i)
                    for num in range(0, len(data[name])):
                        new_worksheet.write(rows_old, num, data[name][num])
                    new_workbook.save(os_path)
