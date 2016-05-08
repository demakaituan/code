import xlrd
excel = xlrd.open_workbook('sheet1.xlsx')
sheet = excel.sheets()[0]     #获取第一个sheet
ncols = sheet.ncols #列数
nrows = sheet.nrows #行数
col_list = []
col_data = 0
for i in range(0,ncols):
    col_data = sheet.col_values(i)
    col_list.append(col_data)
n = ncols/2 #组数
import numpy
def calculate(n,i,j): #参数n表示为第n组数据，参数i为x数据所在的列数，参数j为y数据所在的列数
    print('第' ,n,'组数据')
    x=col_list[i]
    x_var=numpy.var(x)
    x_mean=numpy.mean(x)
    print('x平均值=',x_var)
    print('x方差=',x_mean)
    y=col_list[j]
    y_var=numpy.var(y)
    y_mean=numpy.mean(y)
    print('y平均值=',y_var)
    print('y方差=',y_mean)
    xy=numpy.corrcoef(col_list[i],col_list[j])
    print('xy相关系数=',xy[0,1])#此处发现相关系数的返回值为一个列表

for a in range(0,4):
    n = a+1
    i = 2*a
    j = 2*a+1
    calculate(n,i,j)

import matplotlib.pyplot as plt
import numpy as np
def plot(n): #参数n为第n组
    i = 2*n-2 #x的列数
    j = 2*n-1 #y的列数
    plt.figure(n)
    plt.title('figure') #图表名称
    plt.xlabel('x')     #生成x轴
    plt.ylabel('y')     #生成y轴
    plt.plot(sheet.col_values(i), sheet.col_values(j),'bo')   #作散点图
    x = np.array(sheet.col_values(i))          #numpy.array（）可以进行类型转换，将列表转换为数组类型
    y = np.array(sheet.col_values(j))
    a,b = np.polyfit(x, y, 1)   #调用此函数进行线性拟合计算
    predict_y = a*np.array(x) + b
    plt.plot(x, predict_y)


for i in range(1,n+1):
    plot(i)
plt.show()