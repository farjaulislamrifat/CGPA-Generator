
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFontDatabase ,QFont
from PyQt5 import QtCore
import main
import function
class MainWin(QWidget):
    def s(self, screen):
        super(MainWin, self).s()
        a=23
        QFontDatabase.addApplicationFont('victor mono.ttf')
        self.setFont(QFont('victor mono', 12, italic=True))
        self.boxvlayout = QVBoxLayout()
        self.frame1 = QWidget()
#         self.frame1.setStyleSheet('''
#         QLineEdit{border-radius: 8px;background-color:rgba(0,0,0,0);color:rgba(255,255,255,.5);font-size:14px;border-width: .5px .5px 2px .5px;
#              border-color: #FF6277;
#              border-style: solid;padding: 1px}
#               QLineEdit:focus{background-color:'#200000';border-width: .5px .5px 2px .5px;
#  border-color: #002ef9;
#  border-style: solid;}
#  QLineEdit:hover{border-color: #00ffff;
#  border-style: dashed;border-width: 2px 2px 2px 2px;}
#         QPushButton{border-radius: 8px;background-color:rgba(0,0,0,.3);color:'#ffff10';font-size:23px;border-width: .5px .5px 2px .5px;
#  border-color: #002ef9;
#  border-style: solid;}
#             QPushButton:hover{background-color:'#22A7E7';}
#             QPushButton:pressed{background-color:'#22A700';}
#         ''')
        self.heading1 = QLabel()
        self.heading1.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        self.heading1.setText('Student Details')
        self.heading1.setGeometry()

        # ================global veriable=================
        

        global studentdetailname
        global studentdetailroll
        global writtenlinee1
        global writtenlinee2
        global writtenlinee3
        global writtenlinee4
        global writtenlinee5
        global writtenlinee6
        global writtenlinee7
        global writtenlinee8
        global writtenlinee9
        global writtenlinee10
        global writtenlinee11
        global writtenlinee12
        global mcqlinee1
        global mcqlinee2
        global mcqlinee3
        global mcqlinee4
        global mcqlinee5
        global mcqlinee6
        global mcqlinee7
        global mcqlinee8
        global mcqlinee9
        global mcqlinee10
        global mcqlinee11
        global mcqlinee12
        global practiallinee1
        global practiallinee2
        global practiallinee3
        global practiallinee4
        global practiallinee5
        global practiallinee6
        global practiallinee7
        global practiallinee8
        global practiallinee9
        global practiallinee10
        global practiallinee11
        global practiallinee12
        global totallinee2
        global totallinee4
        global totallinee5
        global totallinee6 
        global totallinee7
        global totallinee8
        global totallinee9
        global totallinee10
        global totallinee11
        global totallinee12
        global totallinee13
        global gplinee2
        global gplinee4
        global gplinee5
        global gplinee6
        global gplinee7
        global gplinee8
        global gplinee9
        global gplinee10
        global gplinee11
        global gplinee12
        global gplinee13
        global gradelinee2
        global gradelinee4
        global gradelinee5
        global gradelinee6
        global gradelinee7
        global gradelinee8
        global gradelinee9
        global gradelinee10
        global gradelinee11
        global gradelinee12
        global gradelinee13
            

        studentdetailname = QLineEdit()
        studentdetailname.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
      
        studentdetailroll = QLineEdit()
        studentdetailroll.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)

        resultspin = QComboBox(self)
        resultspin.setStyleSheet("""border-radius: 8px;background-color:rgba(0,0,0,0);font-size:17px;color:'#ffffff';border-width: .5px .5px 2px .5px;
             border-color: #002ef9;
             border-style: solid;padding : 5px;""")

        self.deletedata = QPushButton('Delete', clicked=lambda: function.databagerow_delete(resultspin.currentText()),
                                      font=QFont('victor mono', 15, italic=True))
        self.studentdetailstart = QPushButton('Start', clicked=lambda:function.start() ,
                                              font=QFont('victor mono', 15, italic=True))
        self.studentdetailreset = QPushButton('Reset', clicked=lambda: function.reset(),
                                              font=QFont('victor mono', 15, italic=True))
       
        self.boxhlayout = QHBoxLayout(self.frame1)
        self.boxvlayout1 = QVBoxLayout()
        self.boxvlafrom = QFormLayout()
        self.boxvlafrom.addRow(QLabel(text="Name's", font=QFont('victor mono', 12, italic=True)),
                               studentdetailname)
       
        self.boxvlafrom.addRow(QLabel(text="Roll", font=QFont(
            'victor mono', 12, italic=True)), studentdetailroll)
        self.boxvlayout2 = QVBoxLayout()
        self.grid2 = QGridLayout()
        
        writtenlinee1 = QLineEdit()
        writtenlinee1.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee2 = QLineEdit()
        writtenlinee2.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee3 = QLineEdit()
        writtenlinee3.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee4 = QLineEdit()
        writtenlinee4.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee5 = QLineEdit()
        writtenlinee5.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee6 = QLineEdit()
        writtenlinee6.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee7 = QLineEdit()
        writtenlinee7.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee8 = QLineEdit()
        writtenlinee8.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee9 = QLineEdit()
        writtenlinee9.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee10 = QLineEdit()
        writtenlinee10.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee11 = QLineEdit()
        writtenlinee11.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        writtenlinee12 = QLineEdit()
        writtenlinee12.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee1 = QLineEdit()
        mcqlinee1.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee2 = QLineEdit()
        mcqlinee2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee3 = QLineEdit(readOnly=True)
        mcqlinee3.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee4 = QLineEdit(readOnly=True)
        mcqlinee4.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee3.setText('X')
        mcqlinee4.setText('X')
        mcqlinee5 = QLineEdit()
        mcqlinee5.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee6 = QLineEdit()
        mcqlinee6.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee7 = QLineEdit()
        mcqlinee7.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee8 = QLineEdit()
        mcqlinee8.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee9 = QLineEdit()
        mcqlinee9.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee10 = QLineEdit()
        mcqlinee10.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee11 = QLineEdit()
        mcqlinee11.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        mcqlinee12 = QLineEdit()
        mcqlinee12.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee1 = QLineEdit(readOnly=True)
        practiallinee1.setText('X')
        practiallinee1.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee2 = QLineEdit(readOnly=True)
        practiallinee2.setText('X')
        practiallinee2.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee3 = QLineEdit(readOnly=True)
        practiallinee3.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee4 = QLineEdit(readOnly=True)
        practiallinee4.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee3.setText('X')
        practiallinee4.setText('X')
        practiallinee5 = QLineEdit(readOnly=True)
        practiallinee5.setText('X')
        practiallinee5.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee6 = QLineEdit()
        practiallinee6.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee7 = QLineEdit()
        practiallinee7.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee8 = QLineEdit()
        practiallinee8.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee9 = QLineEdit(readOnly=True)
        practiallinee9.setText('X')
        practiallinee9.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee10 = QLineEdit(readOnly=True)
        practiallinee10.setText('X')
        practiallinee10.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee11 = QLineEdit()
        practiallinee11.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        practiallinee12 = QLineEdit()
        practiallinee12.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee2 = QLineEdit(readOnly=True)
        sizePolicy = QSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        totallinee2.setSizePolicy(sizePolicy)
        totallinee2.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee4 = QLineEdit(readOnly=True)
        totallinee4.setSizePolicy(sizePolicy)
        totallinee4.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee5 = QLineEdit(readOnly=True)
        totallinee5.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee6 = QLineEdit(readOnly=True)
        totallinee6.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee7 = QLineEdit(readOnly=True)
        totallinee7.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee8 = QLineEdit(readOnly=True)
        totallinee8.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee9 = QLineEdit(readOnly=True)
        totallinee9.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee10 = QLineEdit(readOnly=True)
        totallinee10.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee11 = QLineEdit(readOnly=True)
        totallinee11.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee12 = QLineEdit(readOnly=True)
        totallinee13 = QLineEdit(readOnly=True)
        totallinee12.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        totallinee13.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee2 = QLineEdit(readOnly=True)
        gplinee2.setSizePolicy(sizePolicy)
        gplinee2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee4 = QLineEdit(readOnly=True)
        gplinee4.setSizePolicy(sizePolicy)
        gplinee4.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee5 = QLineEdit(readOnly=True)
        gplinee5.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee6 = QLineEdit(readOnly=True)
        gplinee6.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee7 = QLineEdit(readOnly=True)
        gplinee7.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee8 = QLineEdit(readOnly=True)
        gplinee8.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee9 = QLineEdit(readOnly=True)
        gplinee9.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee10 = QLineEdit(readOnly=True)
        gplinee10.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee11 = QLineEdit(readOnly=True)
        gplinee11.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee12 = QLineEdit(readOnly=True)
        gplinee12.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gplinee13 = QLineEdit(readOnly=True)
        gplinee13.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee2 = QLineEdit(readOnly=True)
        gradelinee2.setSizePolicy(sizePolicy)
        gradelinee2.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee4 = QLineEdit(readOnly=True)
        gradelinee4.setSizePolicy(sizePolicy)
        gradelinee4.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee5 = QLineEdit(readOnly=True)
        gradelinee5.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee6 = QLineEdit(readOnly=True)
        gradelinee6.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee7 = QLineEdit(readOnly=True)
        gradelinee7.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee8 = QLineEdit(readOnly=True)
        gradelinee8.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee9 = QLineEdit(readOnly=True)
        gradelinee9.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee10 = QLineEdit(readOnly=True)
        gradelinee10.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee11 = QLineEdit(readOnly=True)
        gradelinee11.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee12 = QLineEdit(readOnly=True)
        gradelinee12.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
        gradelinee13 = QLineEdit(readOnly=True)
        gradelinee13.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
            
        self.grid2.addWidget(QLabel(text='Stbjects', font=QFont('victor mono', 15, italic=True)), 0, 0, 1, 1,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(totallinee2, 1, 4, 2, 1)
        self.grid2.addWidget(gplinee2, 1, 5, 2, 1)
        self.grid2.addWidget(gradelinee2, 1, 6, 2, 1)
        self.grid2.addWidget(QLabel(text='English 1st', font=QFont(
            'victor mono', 12, italic=True)), 3, 0)
        self.grid2.addWidget(writtenlinee3, 3, 1)
        self.grid2.addWidget(mcqlinee3, 3, 2)
        self.grid2.addWidget(practiallinee3, 3, 3)
        self.grid2.addWidget(QLabel(text='English 2st', font=QFont(
            'victor mono', 12, italic=True)), 4, 0)
        self.grid2.addWidget(writtenlinee4, 4, 1)
        self.grid2.addWidget(mcqlinee4, 4, 2)
        self.grid2.addWidget(practiallinee4, 4, 3)
        self.grid2.addWidget(totallinee4, 3, 4, 2, 1)
        self.grid2.addWidget(gplinee4, 3, 5, 2, 1)
        self.grid2.addWidget(gradelinee4, 3, 6, 2, 1)
        self.grid2.addWidget(QLabel(text='Math       ', font=QFont(
            'victor mono', 12, italic=True)), 5, 0)
        self.grid2.addWidget(writtenlinee5, 5, 1)
        self.grid2.addWidget(mcqlinee5, 5, 2)
        self.grid2.addWidget(practiallinee5, 5, 3)
        self.grid2.addWidget(totallinee5, 5, 4)
        self.grid2.addWidget(gplinee5, 5, 5)
        self.grid2.addWidget(gradelinee5, 5, 6)
        self.grid2.addWidget(QLabel(text='Physics    ', font=QFont(
            'victor mono', 12, italic=True)), 6, 0)
        self.grid2.addWidget(writtenlinee6, 6, 1)
        self.grid2.addWidget(mcqlinee6, 6, 2)
        self.grid2.addWidget(practiallinee6, 6, 3)
        self.grid2.addWidget(totallinee6, 6, 4)
        self.grid2.addWidget(gplinee6, 6, 5)
        self.grid2.addWidget(gradelinee6, 6, 6)
        self.grid2.addWidget(QLabel(text='Chemistry  ', font=QFont(
            'victor mono', 12, italic=True)), 7, 0)
        self.grid2.addWidget(writtenlinee7, 7, 1)
        self.grid2.addWidget(mcqlinee7, 7, 2)
        self.grid2.addWidget(practiallinee7, 7, 3)
        self.grid2.addWidget(totallinee7, 7, 4)
        self.grid2.addWidget(gplinee7, 7, 5)
        self.grid2.addWidget(gradelinee7, 7, 6)
        self.grid2.addWidget(QLabel(text='Biology    ', font=QFont(
            'victor mono', 12, italic=True)), 8, 0)
        self.grid2.addWidget(writtenlinee8, 8, 1)
        self.grid2.addWidget(mcqlinee8, 8, 2)
        self.grid2.addWidget(practiallinee8, 8, 3)
        self.grid2.addWidget(totallinee8, 8, 4)
        self.grid2.addWidget(gplinee8, 8, 5)
        self.grid2.addWidget(gradelinee8, 8, 6)
        self.grid2.addWidget(QLabel(text='BGS        ', font=QFont(
            'victor mono', 12, italic=True)), 9, 0)
        self.grid2.addWidget(writtenlinee9, 9, 1)
        self.grid2.addWidget(mcqlinee9, 9, 2)
        self.grid2.addWidget(practiallinee9, 9, 3)
        self.grid2.addWidget(totallinee9, 9, 4)
        self.grid2.addWidget(gplinee9, 9, 5)
        self.grid2.addWidget(gradelinee9, 9, 6)
        self.grid2.addWidget(QLabel(text='Islam      ', font=QFont(
            'victor mono', 12, italic=True)), 10, 0)
        self.grid2.addWidget(writtenlinee10, 10, 1)
        self.grid2.addWidget(mcqlinee10, 10, 2)
        self.grid2.addWidget(practiallinee10, 10, 3)
        self.grid2.addWidget(totallinee10, 10, 4)
        self.grid2.addWidget(gplinee10, 10, 5)
        self.grid2.addWidget(gradelinee10, 10, 6)
        self.grid2.addWidget(QLabel(text='Physical E.', font=QFont(
            'victor mono', 12, italic=True)), 11, 0)
        self.grid2.addWidget(writtenlinee11, 11, 1)
        self.grid2.addWidget(mcqlinee11, 11, 2)
        self.grid2.addWidget(practiallinee11, 11, 3)
        self.grid2.addWidget(totallinee11, 11, 4)
        self.grid2.addWidget(gplinee11, 11, 5)
        self.grid2.addWidget(gradelinee11, 11, 6)
        self.grid2.addWidget(QLabel(text='Higher Math', font=QFont(
            'victor mono', 12, italic=True)), 12, 0)
        self.grid2.addWidget(writtenlinee12, 12, 1)
        self.grid2.addWidget(mcqlinee12, 12, 2)
        self.grid2.addWidget(practiallinee12, 12, 3)
        self.grid2.addWidget(totallinee12, 12, 4)
        self.grid2.addWidget(QLabel(text='Total Marks', font=QFont('victor mono', 12, italic=True)), 13, 4,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(totallinee13, 14, 4)
        self.grid2.addWidget(QLabel(text='GPA', font=QFont('victor mono', 12, italic=True)), 13, 5,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(gplinee13, 14, 5)
        self.grid2.addWidget(QLabel(text='Main Grade', font=QFont('victor mono', 12, italic=True)), 13, 6,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(gradelinee13, 14, 6)
        self.grid2.addWidget(gplinee12, 12, 5)
        self.grid2.addWidget(gradelinee12, 12, 6)
        self.boxvlayout2.addLayout(self.grid2)
        self.grid2.addWidget(QLabel(text='written', font=QFont('victor mono', 15, italic=True)), 0, 1, 1, 1,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(QLabel(text='  MCQ  ', font=QFont('victor mono', 15, italic=True)), 0, 2, 1, 1,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(QLabel(text='Practial', font=QFont('victor mono', 15, italic=True)), 0, 3, 1, 1,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(QLabel(text='Total', font=QFont('victor mono', 15, italic=True)), 0, 4, 1, 1,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(QLabel(text='GP', font=QFont('victor mono', 15, italic=True)), 0, 5, 1, 1,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(QLabel(text='Grade', font=QFont('victor mono', 15, italic=True)), 0, 6, 1, 1,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(QLabel(text='Bangla 1st ', font=QFont('victor mono', 12, italic=True)), 1, 0, 1, 1,
                             QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.grid2.addWidget(writtenlinee1, 1, 1, 1, 1)
        self.grid2.addWidget(mcqlinee1, 1, 2, 1, 1)
        self.grid2.addWidget(practiallinee1, 1, 3, 1, 1)
        self.grid2.addWidget(QLabel(text='Bangla 2st ', font=QFont(
            'victor mono', 12, italic=True)), 2, 0, 1, 1)
        self.grid2.addWidget(writtenlinee2, 2, 1, 1, 1)
        self.grid2.addWidget(mcqlinee2, 2, 2, 1, 1)
        self.grid2.addWidget(practiallinee2, 2, 3, 1, 1)
        # self.boxvlayout1.addWidget( main.message, 1, QtCore.Qt.AlignTop)
        self.boxvlayout1.addWidget(self.heading1, 1, QtCore.Qt.AlignBottom)
        self.boxvlayout1.addLayout(self.boxvlafrom, 2)
        self.boxvlayout1.addWidget(resultspin)
        self.boxvlayout1.addWidget(self.deletedata)
        self.boxvlayout1.addWidget(self.studentdetailstart)
        self.boxvlayout1.addWidget(self.studentdetailreset)
       
        self.boxvlayout.addWidget(self.frame1, 3, QtCore.Qt.AlignTop)
        self.boxhlayout.addLayout(self.boxvlayout2, 5)
        self.boxhlayout.addLayout(self.boxvlayout1, 2)
        self.boxvlayout.addWidget(QLabel('All Results', font=QFont('victor mono', 20, italic=True)), 0,
                                  QtCore.Qt.AlignHCenter)
        global outputtext                          
        outputtext = QTableWidget(self)
        outputtext.setStyleSheet('''
        QTableWidget{background-color:rgba(0,0,0,0); border-radius: 8px; border-width: .5px .5px 2px .5px; 
        border-color: #002ef9;
        border-style: solid;}
        QHeaderView::section { background-color:'black' }


        ''')
        outputtext.setColumnCount(7)
        outputtext.setColumnWidth(0, int(screen/7))
        outputtext.setColumnWidth(1, int(screen/7))
        outputtext.setColumnWidth(2, int(screen/7)-7)
        outputtext.setColumnWidth(3, int(screen/7)-7)
        outputtext.setColumnWidth(4, int(screen/7)-7)
        outputtext.setColumnWidth(5, int(screen/7)-10)
        outputtext.setColumnWidth(6, int(screen/7)-10)

        item = QTableWidgetItem()

        item.setText('Name')
        outputtext.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()

        item.setText("Father's name")
        outputtext.setHorizontalHeaderItem(1, item)

        item = QTableWidgetItem()
        item.setText("Mother's name")
        outputtext.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        item.setText('Roll')
        outputtext.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()

        item.setText('GPA')
        outputtext.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()

        item.setText('Grade')
        outputtext.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()

        item.setText('Total')
        outputtext.setHorizontalHeaderItem(6, item)
        print(self.studentdetailstart.isChecked())
      

        

        
        self.boxvlayout.addWidget(outputtext)

        self.setLayout(self.boxvlayout)

        
