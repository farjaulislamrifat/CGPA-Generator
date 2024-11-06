
from time import sleep
from turtle import screensize
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from PyQt5.QtGui import QFont, QFontDatabase, QIcon
import sys
import os
import qdarkstyle


class windows (QMainWindow):
    def __init__(self):
        super(windows, self).__init__()
        self.setGeometry(0, 0, 1366, 768)
        self.setWindowIcon(QIcon('windowicon.ico'))
        self.setWindowTitle('CGPA Generator')
        # =======================call Widget====================================
        global widgets
        widgets = QWidget(self)

        def afterok():
            print(radio.isChecked())
            #  ======================create layout=========================
            self.boxlayout = QVBoxLayout(widgets)
            gridlayout = QGridLayout(widgets)
            gridlayout.setAlignment(self, QtCore.Qt.AlignTop)
            widgets.setLayout(gridlayout)
            hboxlayout = QHBoxLayout(widgets)
            widgets.setLayout(hboxlayout)
            fromlayout = QFormLayout(widgets)
            widgets.setLayout(fromlayout)
            # ======================message lable======================
            global message
            message = QLabel(widgets)
            message.setText('ygytfythg')
            message.setGeometry(1000, 20, 1300, 1)
            message.setStyleSheet('''QLabel{color:#FF6277}''')
            message.setFont(QFont('victor mono', 15, italic=True))
            message.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
            self.setCentralWidget(widgets)
            QFontDatabase.addApplicationFont('victor mono.ttf')
            widgets.setFont(QFont('victor mono', 12, italic=True))
            fromlayout.addWidget(message)
            # ======================================all heading=================
            # heading 1====================
            self.heading = QLabel(widgets)
            self.heading.setAlignment(
                QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
            self.heading.setText('CGPA Generator')
            self.heading.setMaximumHeight(50)
            self.heading.setFont(QFont('victor mono', 25, 75, italic=True))
            self.boxlayout.addWidget(self.heading, 0, QtCore.Qt.AlignTop)

            # heading 2=======================
            self.heading1 = QLabel(widgets)
            self.heading1.setAlignment(
                QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
            self.heading1.setText('History')

            self.heading1.setFont(QFont('victor mono', 17, 75, italic=True))
            # =========================menu bar=================start==================
            self.menubar = self.menuBar()

            filemenu = self.menubar.addMenu('File')
            editmenu = self.menubar.addMenu('Setting')
            fileAction = QAction('Export to excl', self)
            fileAction.setShortcut('Ctrl+e')
            # fileAction.triggered.connect(lambda: function.save())
            settingAction = QAction('Edit value', self)
            # settingAction.triggered.connect(lambda: function.k())
            filemenu.addAction(fileAction)
            editmenu.addAction(settingAction)
            #    ======================menu bar===================end============================
            dec = {}
            for i in range(12):
                dec[f'write{str(i)}'] = QLineEdit(self)
                dec[f'mcq{str(i)}'] = QLineEdit(self)
                dec[f'prac{str(i)}'] = QLineEdit(self)
                dec[f'total{str(i)}'] = QLineEdit(self, readOnly=True)
                dec[f'gp{str(i)}'] = QLineEdit(self, readOnly=True)
                dec[f'grade{str(i)}'] = QLineEdit(self, readOnly=True)

            # ===================grid add widget=====================================

            for i in range(12):
                dec[f'write{str(i)}'].setAlignment(
                    QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
                dec[f'mcq{str(i)}'].setAlignment(
                    QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
                dec[f'prac{str(i)}'].setAlignment(
                    QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
                if (i > 0 and i <= 1) or (i > 2 and i <= 3):

                    dec[f'total{str(i)}'].setAlignment(
                        QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
                    gridlayout.addWidget(dec[f'total{str(i)}'], i, 4, 2, 1)

                    dec[f'gp{str(i)}'].setAlignment(
                        QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
                    dec[f'grade{str(i)}'].setAlignment(
                        QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
                    gridlayout.addWidget(dec[f'gp{str(i)}'], i, 5, 2, 1)
                    gridlayout.addWidget(dec[f'grade{str(i)}'], i, 6, 2, 1)
                elif i != 0 and i != 2:

                    dec[f'total{str(i)}'].setAlignment(
                        QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
                    gridlayout.addWidget(dec[f'total{str(i)}'], i+1, 4)
                    dec[f'gp{str(i)}'].setAlignment(
                        QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
                    dec[f'grade{str(i)}'].setAlignment(
                        QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
                    gridlayout.addWidget(dec[f'gp{str(i)}'], i+1, 5)
                    gridlayout.addWidget(dec[f'grade{str(i)}'], i+1, 6)

                gridlayout.addWidget(dec[f'write{str(i)}'], i+1, 1)
                gridlayout.addWidget(dec[f'mcq{str(i)}'], i+1, 2)
                gridlayout.addWidget(dec[f'prac{str(i)}'], i+1, 3)
            gridlayout.addWidget(QLabel(text='Bangla 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 1, 0)
            gridlayout.addWidget(QLabel(text='Bangla 2st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 2, 0)
            gridlayout.addWidget(QLabel(text='English 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 3, 0)
            gridlayout.addWidget(QLabel(text='English 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 4, 0)
            gridlayout.addWidget(QLabel(text='English 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 5, 0)
            gridlayout.addWidget(QLabel(text='English 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 6, 0)
            gridlayout.addWidget(QLabel(text='English 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 7, 0)
            gridlayout.addWidget(QLabel(text='English 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 8, 0)
            gridlayout.addWidget(QLabel(text='English 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 9, 0)
            gridlayout.addWidget(QLabel(text='English 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 10, 0)
            gridlayout.addWidget(QLabel(text='English 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 11, 0)
            gridlayout.addWidget(QLabel(text='English 1st', alignment=QtCore.Qt.AlignCenter |
                                 QtCore.Qt.AlignLeft, font=QFont('victor mono', 12, italic=True)), 12, 0)
            sizePolicy = QSizePolicy(
                QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
            sizePolicy.setHorizontalStretch(1)
            sizePolicy.setVerticalStretch(0)
            dec['total1'].setSizePolicy(sizePolicy)
            dec['gp1'].setSizePolicy(sizePolicy)
            dec['grade1'].setSizePolicy(sizePolicy)
            dec['total3'].setSizePolicy(sizePolicy)
            dec['gp3'].setSizePolicy(sizePolicy)
            dec['grade3'].setSizePolicy(sizePolicy)

            gridlayout.addWidget(QLabel(
                text='subjects', alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter, font=QFont('victor mono', 12, italic=True)), 0, 0)
            gridlayout.addWidget(QLabel(
                text='Writen', alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter, font=QFont('victor mono', 12, italic=True)), 0, 1)
            gridlayout.addWidget(QLabel(
                text='MCQ', alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter, font=QFont('victor mono', 12, italic=True)), 0, 2)
            gridlayout.addWidget(QLabel(
                text='Practical', alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter, font=QFont('victor mono', 12, italic=True)), 0, 3)
            gridlayout.addWidget(QLabel(
                text='Total', alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter, font=QFont('victor mono', 12, italic=True)), 0, 4)
            gridlayout.addWidget(QLabel(
                text='GP', alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter, font=QFont('victor mono', 12, italic=True)), 0, 5)
            gridlayout.addWidget(QLabel(
                text='Grade', alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter, font=QFont('victor mono', 12, italic=True)), 0, 6)

            tabwidget = QTableWidget()
            tabwidget.setColumnCount(5)
            tabwidget.setColumnWidth(0, int(screen/5))
            tabwidget.setColumnWidth(1, int(screen/5))
            tabwidget.setColumnWidth(2, int(screen/5))
            tabwidget.setColumnWidth(3, int(screen/5))
            tabwidget.setColumnWidth(4, int(screen/5))
            tabwidget.setRowCount(10)

            # add tableitem

            item = QTableWidgetItem()
            item.setText('Name')
            tabwidget.setHorizontalHeaderItem(0, item)
            item = QTableWidgetItem()
            item.setText('Roll')
            tabwidget.setHorizontalHeaderItem(1, item)
            item = QTableWidgetItem()
            item.setText('Total')
            tabwidget.setHorizontalHeaderItem(2, item)
            item = QTableWidgetItem()
            item.setText('GPA')
            tabwidget.setHorizontalHeaderItem(3, item)
            item = QTableWidgetItem()
            item.setText('Grade')
            tabwidget.setHorizontalHeaderItem(4, item)

            # ===================== hboxlayout add layout   ============================
            hboxlayout.addLayout(gridlayout, 3)
            hboxlayout.addLayout(fromlayout, 1)
            # ===========================add layout hboxlayout=================
            # self.boxlayout.addWidget(message, 0)
            self.boxlayout.addLayout(hboxlayout, 1)
            self.boxlayout.addWidget(self.heading1, 0)
            self.boxlayout.addWidget(tabwidget, 1)
            # self.boxlayout.addWidget(message, 5, alignment=QtCore.Qt.AlignTop)
            # =============================== set layout==================================
            widgets.setLayout(self.boxlayout)
            # ===========================show window=========================

        self.show()

        def topWin():
            dil = QDialog()
            dil.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
            dil.setWindowIcon(QIcon('windowicon.ico'))
            dil.setWindowTitle('CGPA Generator')
            dil.setGeometry(550, 250, 300, 20)

            QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

            dil.buttonBox = QDialogButtonBox(QBtn)
            dil.buttonBox.accepted.connect(lambda: ok())
            dil.buttonBox.rejected.connect(lambda: close())

            def close():
                os._exit(0)

            def ok():
                if radio1.isChecked() == True or radio.isChecked() == True:
                    afterok()
                    dil.close()

            QFontDatabase.addApplicationFont('victor mono.ttf')
            dil.setFont(QFont('victor mono', 14, italic=True))

            vbox = QVBoxLayout(self)
            global radio , radio1
            radio = QRadioButton(self)

            radio.setText('Scince')

            radio1 = QRadioButton(self)

            radio1.setText('Humanities')

            vbox.addWidget(QLabel(text='Choose a Subject',
                           alignment=QtCore.Qt.AlignTop), 0, alignment=QtCore.Qt.AlignHCenter)
            vbox.addWidget(radio, 0, alignment=QtCore.Qt.AlignHCenter)
            vbox.addWidget(radio1, 0, alignment=QtCore.Qt.AlignHCenter)
            vbox.addWidget(dil.buttonBox, 0)
            dil.setLayout(vbox)

            dil.exec_()
        topWin()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    darkstyle = qdarkstyle.load_stylesheet_pyqt5()

    app.setStyleSheet(darkstyle)
    screen = app.primaryScreen().geometry().width()-70
    win = windows()
    os._exit(app.exec_())
