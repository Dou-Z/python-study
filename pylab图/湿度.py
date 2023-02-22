from matplotlib import pyplot
import matplotlib.pyplot as plt

names = range(0, 24,2)
names = [str(x) for x in list(names)]
print(names)
x = range(len(names))
y_train = [25,26,33,30,28,25,20,18,22,27,32,35]

plt.plot(x, y_train, marker='o', mec='r', mfc='w', label='HUM')
# plt.plot(x, y_test, marker='*', ms=10, label='uniprot90_test')
plt.legend()  # 让图例生效
# 将x轴的各标签旋转1度
plt.xticks(x, names, rotation=1)


plt.margins(0)
plt.subplots_adjust(bottom=0.10)
plt.xlabel('time/(H)') #X轴标签
plt.ylabel("HUM/(℃)") #Y轴标签
pyplot.yticks([10,15, 20,25, 30, 35])
#plt.title("A simple plot") #标题
plt.savefig('HUM.jpg',dpi = 900)