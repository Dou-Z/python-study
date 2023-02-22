# encoding=utf-8
from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np

names = range(0, 24,1)
names = [int(x) for x in list(names)]
print(names)
x = range(len(names))

y_train = [19.8,19.7,19.6,19.5,19.5,19.3,19.4,19.7,20.0,20.1,20.2,20.5,20.7,21.0,21.6,21.5,21.4,20.9,20.5,20.2,20.2,20.1,19.9,19.5]
y_test = [23,24,25,25,24,23,22,22,21,21,20,20,20,19,20,21,22,23,24,23,24,24,25,25]
# plt.plot(x, y, 'ro-')
# plt.plot(x, y1, 'bo-')
# pl.xlim(-1, 11)  # 限定横轴的范围
# pl.ylim(-1, 110)  # 限定纵轴的范围

plt.plot(x, y_train, marker='o', mec='r', mfc='w', label='TEMP')
plt.plot(x, y_test, marker='*', ms=10, label='HUM')
plt.legend()  # 让图例生效
# 将x轴的各标签旋转1度
plt.xticks(x, names, rotation=1)


plt.margins(0)
plt.subplots_adjust(bottom=0.10)
plt.xlabel('time/(H)') #X轴标签
plt.ylabel("temp/HUM") #Y轴标签
pyplot.yticks([18,19,20,21,22,23,24,25,26,27])
#plt.title("A simple plot") #标题
plt.savefig('wendu.jpg',dpi = 1080)