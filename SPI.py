import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import time

class TableView(QWidget):#创建窗口Qwidget
    def __init__(self,arg=None):#构造函数
        super(TableView,self).__init__(arg)#初始化父类构造函数
        self.setWindowTitle("SPI_AI复判")#窗体设置标题
        self.resize(1050,600)#设置窗体尺寸
        self.model=QStandardItemModel(4,8)#创建模型
        self.model.setHorizontalHeaderLabels(['shiftX','shiftY','Per_H','Per_A','Per_V','Bridge','Padgroup','AI_ReCheck'])#配置mode的headerlabel
        self.tableview=QTableView()#创建table_view控件
        self.tableview.setModel(self.model)#为table_view配置model
        self.pushButton = QPushButton('启动',self)
        self.pushButton.setGeometry(QRect(300, 300, 400, 400))
        self.pushButton.setObjectName("pushButton")
        layout_v=QVBoxLayout()#创建布局
        layout_v.addWidget(self.tableview)#布局里增加控件
        # layout_h=QHBoxLayout()
        # layout_h.addWidget(self.pushButton)
        self.setLayout(layout_v)#self窗体增加布局
        # self.setLayout(layout_h)#self窗体增加布局
        #获取数据
        thread=BackendThread()
        data=thread.get_data()
        item11=QStandardItem('10')
        item12=QStandardItem('雷神')
        item13=QStandardItem('1000')
        self.model.setItem(0,0,item11)
        self.model.setItem(0,1,item12)
        self.model.setItem(0,2,item13)

class BackendThread(QThread):#起一个子进程
    data_signal=pyqtSignal(dict)#起一个信号
    def get_data(self):
        a = np.random.rand(1, 5)
        b = np.zeros((1, 1))
        meta_data = np.hstack((a, b))[0]
        dic = {}
        dic['shiftX'] = meta_data[0]
        dic['shiftY'] = meta_data[1]
        dic['H'] = meta_data[2]
        dic['A'] = meta_data[3]
        dic['V'] = meta_data[4]
        dic['Bridge'] = meta_data[5]
        dic['Padgroup'] = 'U66000-1'
        data = {}
        data['data_set'] = [dic, dic]
        return data

    def run(self):
        while True:#不停获取系统时间，和发送信号
            data=self.get_data()
            self.data_signal.emit(data)
            time.sleep(1)


if __name__=="__main__":
    app=QApplication(sys.argv)
    main=TableView()
    main.show()
    sys.exit(app.exec_())