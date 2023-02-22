import xlrd
import xlwt
import matplotlib.pyplot as plt



def read_excel():
    # 打开文件
    workBook = xlrd.open_workbook('D:\PYTHON\爬虫\爬虫课堂\课堂内容\数据\去哪儿数据.xls');

    # 1.获取sheet的名字
    # 1.1 获取所有sheet的名字(list类型)
    allSheetNames = workBook.sheet_names();
    print(allSheetNames);

    # 1.2 按索引号获取sheet的名字（string类型）
    sheet1Name = workBook.sheet_names()[0];
    print(sheet1Name);

    # 2. 获取sheet内容
    ## 2.1 法1：按索引号获取sheet内容
    sheet1_content1 = workBook.sheet_by_index(0); # sheet索引从0开始
    ## 2.2 法2：按sheet名字获取sheet内容
    sheet1_content2 = workBook.sheet_by_name('游记详情');
    #
    # 3. sheet的名称，行数，列数
    print(sheet1_content1.name,sheet1_content1.nrows,sheet1_content1.ncols);

    # 4. 获取整行和整列的值（数组）
    rows = sheet1_content1.row_values(3); # 获取第四行内容
    cols = sheet1_content1.col_values(2); # 获取第三列内容
    # print(cols);
    # plot_days(cols)
def plot_days(cols):
    day_list = ['共1天','共2天','共3天','共4天','共5天','共6天','共7天','共8天','共9天']
    day_data = [0 for _ in range(9)]
    for i in cols[1:]:
        # print(i[1])
        day_data[0] += 1 if int(i[1]) == 1 else 0
        day_data[1] += 1 if int(i[1]) == 2 else 0
        day_data[2] += 1 if int(i[1]) == 3 else 0
        day_data[3] += 1 if int(i[1]) == 4 else 0
        day_data[4] += 1 if int(i[1]) == 5 else 0
        day_data[5] += 1 if int(i[1]) == 6 else 0
        day_data[6] += 1 if int(i[1]) == 7 else 0
        day_data[7] += 1 if int(i[1]) == 8 else 0
        day_data[8] += 1 if int(i[1]) == 9 else 0

    print(day_data)
    # 绘制柱状图
    plt.bar(x=day_list, height=day_data, color="green", width=0.5)
    # 显示柱状图形的值
    for x, y in zip(day_list, day_data):
        plt.text(x, y + sum(day_data) // 50, "%d" % y, ha="center", va="top")
    plt.xlabel("天数")
    plt.ylabel("单位/次数")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.savefig("days.jpg")
    print("已保存为days.jpg！")

    # 5. 获取单元格内容(三种方式)
    # print(sheet1_content1.cell(1, 0).value);
    # print(sheet1_content1.cell_value(2, 2));
    # print(sheet1_content1.row(2)[2].value);
    #
    # # 6. 获取单元格内容的数据类型
    # # Tips: python读取excel中单元格的内容返回的有5种类型 [0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error]
    # print(sheet1_content1.cell(5, 1).ctype);


# if __name__ == '__main__':
#     read_excel();
