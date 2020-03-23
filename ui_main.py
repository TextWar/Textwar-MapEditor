# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.paintTextNum = 1
        self.paintTextTx = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.dockWidgetContents)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_6 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_6.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_6.setObjectName("dockWidget_6")
        self.dockWidgetContents_6 = QtWidgets.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.dockWidgetContents_6)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.pushButton_5 = QtWidgets.QPushButton(self.dockWidgetContents_6)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.dockWidget_6.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_6)
        self.dockWidget_5 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_5.setFloating(False)
        self.dockWidget_5.setObjectName("dockWidget_5")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.dockWidgetContents_5)
        self.tableWidget_2.setAlternatingRowColors(False)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_2.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(20)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(16)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(27)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(14)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.dockWidget_5.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_5)
        self.dockWidget_7 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_7.setObjectName("dockWidget_7")
        self.dockWidgetContents_7 = QtWidgets.QWidget()
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.dockWidgetContents_7)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.dockWidgetContents_7)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.dockWidgetContents_7)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_7 = QtWidgets.QPushButton(self.dockWidgetContents_7)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7)
        self.dockWidget_7.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_7)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())


        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.hashMapRemoveRow)
        self.pushButton.clicked.connect(self.hashMapInsertRow)
        self.pushButton_3.clicked.connect(self.mapInsertRow)
        self.pushButton_4.clicked.connect(self.mapRemoveRow)
        self.pushButton_6.clicked.connect(self.mapInsertColumn)
        self.pushButton_7.clicked.connect(self.mapRemoveColumn)
        self.action.triggered.connect(self.File_Selector)
        self.pushButton_5.clicked.connect(self.generate)
        self.tableWidget.itemClicked.connect(self.paintText)
        self.tableWidget_2.itemSelectionChanged.connect(self.paintMap)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def File_Selector(self):
        filename = QFileDialog.getOpenFileName(self.MainWindow, "选择*.json地图文件", "", "Json Files (*.json)")
        while filename[0] == '':
            filename = QFileDialog.getOpenFileName(self.MainWindow, "选择*.json地图文件", "", "Json Files (*.json)")
        import json
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)
        json__ = json.load(open(filename[0],"r"))
        for i,str_ in enumerate(json__["hashmap"]):
            self.tableWidget.insertRow(i)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str_)
            self.tableWidget.setItem(i,0,item)
        for i in range(0, len(json__["map"][0])):
            self.tableWidget_2.insertColumn(self.tableWidget_2.columnCount())
        for i,c in enumerate(json__["map"]):
            self.tableWidget_2.insertRow(self.tableWidget_2.rowCount())
            for ib,str__ in enumerate(c):
                item = QtWidgets.QTableWidgetItem()
                for row2 in range(self.tableWidget.rowCount()):
                    if str(row2) == str(str__):
                        item.setText(self.tableWidget.item(row2, 0).text())
                self.tableWidget_2.setItem(i,ib,item)

    def generate(self):
        try:
            data = []
            hash_map = []
            for row in range(self.tableWidget_2.rowCount()):
                data.append([])
                for column in range(self.tableWidget_2.columnCount()):
                    for row2 in range(self.tableWidget.rowCount()):
                        if self.tableWidget.item(row2, 0).text() == self.tableWidget_2.item(row,column).text():
                            data[row].append(row2)
            for row2 in range(self.tableWidget.rowCount()):
                dict_ = dict()[row2] = self.tableWidget.item(row2, 0).text()
                hash_map.append(dict_)
            a = {"hashmap": hash_map, "type": 1, "name": "some", "author": "someone behind the screen", "version": "b1",
                 "map": data}
            import json
            json_ = json.dumps(a)
            self.textBrowser.setText(json_)
        except Exception as e:
            self.textBrowser.setText("发生了一个错误！　请检查是否有留空")
    def paintText(self,a):
        self.paintTextTx = a.text()
        self.paintTextNum = a.row()+1
    def paintMap(self):
        for index in self.tableWidget_2.selectedIndexes():
            item = QtWidgets.QTableWidgetItem()
            item.setText(self.paintTextTx)
            self.tableWidget_2.setItem(index.row(),index.column(),item)
            # item.set
            # self.tableWidget_2.edit
            # self.tableWidget_2.itemFromIndex(index).setText("a")
            # item.setText("s")
    def mapInsertRow(self):
        self.tableWidget_2.insertRow(self.tableWidget_2.rowCount())
    def mapRemoveRow(self):
        self.tableWidget_2.removeRow(self.tableWidget_2.rowCount()-1)
    def mapInsertColumn(self):
        self.tableWidget_2.insertColumn(self.tableWidget_2.columnCount())
    def mapRemoveColumn(self):
        self.tableWidget_2.removeColumn(self.tableWidget_2.columnCount()-1)

    def hashMapInsertRow(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())
    def hashMapRemoveRow(self):
        self.tableWidget.removeRow(self.tableWidget.rowCount()-1)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget_2.setSortingEnabled(False)
        self.pushButton.setText(_translate("MainWindow", "添加行"))
        self.pushButton_2.setText(_translate("MainWindow", "减少行"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "映射表"))
        self.tableWidget.setSortingEnabled(False)
        self.pushButton_3.setText(_translate("MainWindow", "添加行"))
        self.pushButton_4.setText(_translate("MainWindow", "减少行"))
        self.pushButton_6.setText(_translate("MainWindow", "添加列"))
        self.pushButton_7.setText(_translate("MainWindow", "减少列"))
        self.action.setText(_translate("MainWindow", "读取"))
        self.pushButton_5.setText(_translate("MainWindow", "生成"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dockWidget_5.setWindowTitle(_translate("MainWindow", "地图"))
        self.dockWidget_6.setWindowTitle(_translate("MainWindow", "结果"))
        self.dockWidget_7.setWindowTitle(_translate("MainWindow", "操作"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "映射表"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.tableWidget_2.clear()
