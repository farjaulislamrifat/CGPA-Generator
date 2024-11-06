import imp
import sqlite3
import se
from time import sleep
import PyQt5.QtWidgets as w
import main
from threading import Thread
from scince import *
con = False

def messagetext(text ):
            main.message.setText(text)
            sleep(5)
            main.message.setText(' ')
messagetext('jd')
def databagesave( name, father_name, mother_name, roll, total, gpa, grade):
    try:
        connect = sqlite3.connect('result.db')
        cur = connect.cursor()

        cur.execute(f""" 
        INSERT INTO result VALUES('{name}' , '{father_name}' , '{mother_name}' , '{roll}' , '{gpa}' , '{grade}' , '{total}')
         """)

        connect.commit()
        connect.close()

    except Exception as er:
        pass

def com(data , output,resultcombo):
            
            r = data

            rows = output.rowCount()
            def rul():
                for ind in range(r.__len__()):
                    resultcombo.addItem(str(r[ind][3]))
            if rows > resultcombo.count():
                
                resultcombo.clear()
                rul()
            elif function.con:
                
                resultcombo.clear()
                rul()
def databage_get():
    try:
        connect = sqlite3.connect('result.db')
        cur = connect.cursor()

        cur.execute("""SELECT * FROM result""")
        g = cur.fetchall()

        connect.commit()
        connect.close()
        return g

    except Exception as er:
        pass

def databagerow_delete(roll):
    try:
       
        connect = sqlite3.connect('result.db')
        cur = connect.cursor()
        
        cur.execute(f""" DELETE FROM result WHERE roll={roll};""")
        
        connect.commit()
        connect.close()
        global con
        con = True

    except Exception as er:
        print(f'fun :{er}')



def k():
    print('ffj')        


# ==========================create excel ========================
# 
#     
def messagetext(text ):
            main.message .setText(text)
            sleep(5)
            main.message.setText(' ')


def save():
            try:
                # scince.Thread(target=lambda: ).start()
                path =w.QFileDialog(main.widgets).getSaveFileName(
                    directory='Project.xlsx', filter='Excel File (*.xlsx)')

                wb = se.Workbook()
                ws = wb.active
                ws['A1'] = 'Roll'
                ws['B1'] = 'Name'
                ws['C1'] = "Father's name"
                ws['D1'] = "Mother's name"
                ws['E1'] = "GPA"
                ws['F1'] = "Grade"
                ws['G1'] = 'Total marks'

                data = function.databage_get()
                for index in range(data.__len__()):
                    da = data[index]

                    ws[f'A{index+2}'] = da[3]

                    ws[f'B{index+2}'] = da[0]
                    ws[f'C{index+2}'] = da[1]
                    ws[f'D{index+2}'] = da[2]
                    ws[f'E{index+2}'] = da[4]
                    ws[f'F{index+2}'] = da[5]
                    ws[f'G{index+2}'] = da[6]

                wb.save(path[0])

                se.Thread(target=lambda:  ('saved successful.')).start()
            except Exception as et:
                print(et)
                se.Thread (target=lambda:se.MainWin.messagetext('Seclect your save directory')).start()

def p(output):

    data1 =databage_get()
    output.setRowCount(data1.__len__())
    for index in range(data1.__len__()):
        for i in range(6):
            items =w.QTableWidgetItem()

            a = data1[index]

            items.setText(a[i])
            output.setItem(index, i, items)
def reset():
            
           
            studentdetailname.setText('')
            studentdetailroll.setText('')
            
            writtenlinee1.setText('')
            writtenlinee2.setText('')
            writtenlinee3.setText('')
            writtenlinee4.setText('')
            writtenlinee5.setText('')
            writtenlinee6.setText('')
            writtenlinee7.setText('')
            writtenlinee8.setText('')
            writtenlinee9.setText('')
            writtenlinee10.setText('')
            writtenlinee11.setText('')
            writtenlinee12.setText('')

            mcqlinee1.setText('')
            mcqlinee2.setText('')

            mcqlinee5.setText('')
            mcqlinee6.setText('')
            mcqlinee7.setText('')
            mcqlinee8.setText('')
            mcqlinee9.setText('')
            mcqlinee10.setText('')
            mcqlinee11.setText('')
            mcqlinee12.setText('')

            practiallinee6.setText('')
            practiallinee7.setText('')
            practiallinee8.setText('')

            practiallinee11.setText('')
            practiallinee12.setText('')

            totallinee2.setText('')
            totallinee4.setText('')
            totallinee5.setText('')
            totallinee6.setText('')
            totallinee7.setText('')
            totallinee8.setText('')
            totallinee9.setText('')
            totallinee10.setText('')
            totallinee11.setText('')
            totallinee12.setText('')
            totallinee13.setText('')

            gplinee2.setText('')
            gplinee4.setText('')
            gplinee5.setText('')
            gplinee6.setText('')
            gplinee7.setText('')
            gplinee8.setText('')
            gplinee9.setText('')
            gplinee10.setText('')
            gplinee11.setText('')
            gplinee12.setText('')
            gplinee13.setText('')

            gradelinee2.setText('')
            gradelinee4.setText('')
            gradelinee5.setText('')
            gradelinee6.setText('')
            gradelinee7.setText('')
            gradelinee8.setText('')
            gradelinee9.setText('')
            gradelinee10.setText('')
            gradelinee11.setText('')
            gradelinee12.setText('')
            gradelinee13.setText('')
            Thread(target=lambda: messagetext('Reset Successfull')).start()


def start():
            
            
            def total():
                try:
                    total1 = int(writtenlinee1.text()) + int(mcqlinee1.text()) + int(writtenlinee2.text()) + int(
                        mcqlinee2.text())
                    totallinee2.setText(str(total1))
                    total2 = int(writtenlinee3.text()) + int(writtenlinee4.text())
                    totallinee4.setText(str(total2))
                    total3 = int(writtenlinee5.text()) + int(mcqlinee5.text())
                    totallinee5.setText(str(total3))
                    total4 = int(writtenlinee6.text()) + \
                        int(mcqlinee6.text()) + int(practiallinee6.text())
                    totallinee6.setText(str(total4))
                    total5 = int(writtenlinee7.text()) + \
                        int(mcqlinee7.text()) + int(practiallinee7.text())
                    totallinee7.setText(str(total5))
                    total6 = int(writtenlinee8.text()) + \
                        int(mcqlinee8.text()) + int(practiallinee8.text())
                    totallinee8.setText(str(total6))
                    total7 = int(writtenlinee9.text()) + int(mcqlinee9.text())
                    totallinee9.setText(str(total7))
                    total8 = int(writtenlinee10.text()) + int(mcqlinee10.text())
                    totallinee10.setText(str(total8))
                    total9 = int(writtenlinee11.text()) + \
                        int(mcqlinee11.text()) + int(practiallinee11.text())
                    totallinee11.setText(str(total9))
                    total10 = int(writtenlinee12.text()) + \
                        int(mcqlinee12.text()) + int(practiallinee12.text())
                    totallinee12.setText(str(total10))
                except:
                    Thread(target=lambda:messagetext('Fill all subjects markes properly')).start()
                if total10 >= 40:
                    totals = total10 - 40
                else:
                    totals = total10
                totallinee13.setText(
                    str(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + totals))
                
                def allsub():
                        def bangla():
                            gp = ''
                            grade = ''
                            if int(writtenlinee1.text()) + int(writtenlinee2.text()) < 40 or int(mcqlinee1.text()) + int(mcqlinee2.text()) < 26:
                                gp = '0.00'
                                grade = 'F'
                            elif total1 >= 66 and total1 < 80:
                                gp = '1.00'
                                grade = 'D'
                            elif total1 >= 80 and total1 < 100:
                                gp = '2.00'
                                grade = 'C'
                            elif total1 >= 100 and total1 < 120:
                                gp = '3.00'
                                grade = 'B'
                            elif total1 >= 120 and total1 < 140:
                                gp = '3.50'
                                grade = 'A-'
                            elif total1 >= 140 and total1 < 160:
                                gp = '4.00'
                                grade = 'A'
                            elif total1 >= 160:
                                gp = '5.00'
                                grade = 'A+'
                            return [gp, grade]

                        def english():
                            gp = ''
                            grade = ''
                            if total2 < 66:
                                gp = '0.00'
                                grade = 'F'
                            elif total2 >= 66 and total2 < 80:
                                gp = '1.00'
                                grade = 'D'
                            elif total2 >= 80 and total2 < 100:
                                gp = '2.00'
                                grade = 'C'
                            elif total2 >= 100 and total2 < 120:
                                gp = '3.00'
                                grade = 'B'
                            elif total2 >= 120 and total2 < 140:
                                gp = '3.50'
                                grade = 'A-'
                            elif total2 >= 140 and total2 < 160:
                                gp = '4.00'
                                grade = 'A'
                            elif total2 >= 160:
                                gp = '5.00'
                                grade = 'A+'
                            return [gp, grade]

                        def math():
                            gp = ''
                            grade = ''
                            if int(writtenlinee5.text()) < 20 or int(mcqlinee5.text()) < 13:
                                gp = '0.00'
                                grade = 'F'
                            elif total3 >= 33 and total3 < 40:
                                gp = '1.00'
                                grade = 'D'
                            elif total3 >= 40 and total3 < 50:
                                gp = '2.00'
                                grade = 'C'
                            elif total3 >= 50 and total3 < 60:
                                gp = '3.00'
                                grade = 'B'
                            elif total3 >= 60 and total3 < 70:
                                gp = '3.50'
                                grade = 'A-'
                            elif total3 >= 70 and total3 < 80:
                                gp = '4.00'
                                grade = 'A'
                            elif total3 >= 80:
                                gp = '5.00'
                                grade = 'A+'
                            return [gp, grade]

                        def pysics():
                            gp = ''
                            grade = ''
                            if int(writtenlinee6.text()) < 13 or int(mcqlinee6.text()) < 12 or int(practiallinee6.text()) < 8:
                                gp = '0.00'
                                grade = 'F'
                            elif total4 >= 33 and total4 < 40:
                                gp = '1.00'
                                grade = 'D'
                            elif total4 >= 40 and total4 < 50:
                                gp = '2.00'
                                grade = 'C'
                            elif total4 >= 50 and total4 < 60:
                                gp = '3.00'
                                grade = 'B'
                            elif total4 >= 60 and total4 < 70:
                                gp = '3.50'
                                grade = 'A-'
                            elif total4 >= 70 and total4 < 80:
                                gp = '4.00'
                                grade = 'A'
                            elif total4 >= 80:
                                gp = '5.00'
                                grade = 'A+'
                            return [gp, grade]

                        def chemistry():
                            gp = ''
                            grade = ''
                            if int(writtenlinee7.text()) < 13 or int(mcqlinee7.text()) < 12 or int(practiallinee7.text()) < 8:
                                gp = '0.00'
                                grade = 'F'
                            elif total5 >= 33 and total5 < 40:
                                gp = '1.00'
                                grade = 'D'
                            elif total5 >= 40 and total5 < 50:
                                gp = '2.00'
                                grade = 'C'
                            elif total5 >= 50 and total5 < 60:
                                gp = '3.00'
                                grade = 'B'
                            elif total5 >= 60 and total5 < 70:
                                gp = '3.50'
                                grade = 'A-'
                            elif total5 >= 70 and total5 < 80:
                                gp = '4.00'
                                grade = 'A'
                            elif total5 >= 80:
                                gp = '5.00'
                                grade = 'A+'
                            return [gp, grade]

                        def biology():
                            gp = ''
                            grade = ''
                            if int(writtenlinee8.text()) < 13 or int(mcqlinee8.text()) < 12 or int(practiallinee8.text()) < 8:
                                gp = '0.00'
                                grade = 'F'
                            elif total6 >= 33 and total6 < 40:
                                gp = '1.00'
                                grade = 'D'
                            elif total6 >= 40 and total6 < 50:
                                gp = '2.00'
                                grade = 'C'
                            elif total6 >= 50 and total6 < 60:
                                gp = '3.00'
                                grade = 'B'
                            elif total6 >= 60 and total6 < 70:
                                gp = '3.50'
                                grade = 'A-'
                            elif total6 >= 70 and total6 < 80:
                                gp = '4.00'
                                grade = 'A'
                            elif total6 >= 80:
                                gp = '5.00'
                                grade = 'A+'
                            return [gp, grade]

                        def bgs():
                            gp = ''
                            grade = ''
                            if int(writtenlinee9.text()) < 20 or int(mcqlinee9.text()) < 13:
                                gp = '0.00'
                                grade = 'F'
                            elif total7 >= 33 and total7 < 40:
                                gp = '1.00'
                                grade = 'D'
                            elif total7 >= 40 and total7 < 50:
                                gp = '2.00'
                                grade = 'C'
                            elif total7 >= 50 and total7 < 60:
                                gp = '3.00'
                                grade = 'B'
                            elif total7 >= 60 and total7 < 70:
                                gp = '3.50'
                                grade = 'A-'
                            elif total7 >= 70 and total7 < 80:
                                gp = '4.00'
                                grade = 'A'
                            elif total7 >= 80:
                                gp = '5.00'
                                grade = 'A+'
                            return [gp, grade]

                        def islam():
                            gp = ''
                            grade = ''
                            if int(writtenlinee10.text()) < 20 or int(mcqlinee10.text()) < 13:
                                gp = '0.00'
                                grade = 'F'
                            elif total8 >= 33 and total8 < 40:
                                gp = '1.00'
                                grade = 'D'
                            elif total8 >= 40 and total8 < 50:
                                gp = '2.00'
                                grade = 'C'
                            elif total8 >= 50 and total8 < 60:
                                gp = '3.00'
                                grade = 'B'
                            elif total8 >= 60 and total8 < 70:
                                gp = '3.50'
                                grade = 'A-'
                            elif total8 >= 70 and total8 < 80:
                                gp = '4.00'
                                grade = 'A'
                            elif total8 >= 80:
                                gp = '5.00'
                                grade = 'A+'
                            return [gp, grade]

                        def physical():
                            gp = ''
                            grade = ''
                            if int(writtenlinee11.text()) < 13 or int(mcqlinee11.text()) < 12 or int(
                                    practiallinee11.text()) < 8:
                                gp = '0.00'
                                grade = 'F'
                            elif total9 >= 33 and total9 < 40:
                                gp = '1.00'
                                grade = 'D'
                            elif total9 >= 40 and total9 < 50:
                                gp = '2.00'
                                grade = 'C'
                            elif total9 >= 50 and total9 < 60:
                                gp = '3.00'
                                grade = 'B'
                            elif total9 >= 60 and total9 < 70:
                                gp = '3.50'
                                grade = 'A-'
                            elif total9 >= 70 and total9 < 80:
                                gp = '4.00'
                                grade = 'A'
                            elif total9 >= 80:
                                gp = '5.00'
                                grade = 'A+'
                            return [gp, grade]

                        def higher_math():
                            gp = ''
                            grade = ''
                            if int(writtenlinee12.text()) < 13 or int(mcqlinee12.text()) < 12 or int(
                                    practiallinee12.text()) < 8:
                                gp = '0.00'
                                grade = 'F'
                            elif total10 >= 33 and total10 < 40:
                                gp = '1.00'
                                grade = 'D'
                            elif total10 >= 40 and total10 < 50:
                                gp = '2.00'
                                grade = 'C'
                            elif total10 >= 50 and total10 < 60:
                                gp = '3.00'
                                grade = 'B'
                            elif total10 >= 60 and total10 < 70:
                                gp = '3.50'
                                grade = 'A-'
                            elif total10 >= 70 and total10 < 80:
                                gp = '4.00'
                                grade = 'A'
                            elif total10 >= 80:
                                gp = '5.00'
                                grade = 'A+'
                            return [gp, grade]
                        bangla = bangla()
                        english = english()
                        math = math()
                        pysics = pysics()
                        chemistry = chemistry()
                        biology = biology()
                        bgs = bgs()
                        islam = islam()
                        physicla = physical()
                        higher_math = higher_math()
                        gplinee2.setText(bangla[0])
                        gradelinee2.setText(bangla[1])
                        gplinee4.setText(english[0])
                        gradelinee4.setText(english[1])
                        gplinee5.setText(math[0])
                        gradelinee5.setText(math[1])
                        gplinee6.setText(pysics[0])
                        gradelinee6.setText(pysics[1])
                        gplinee7.setText(chemistry[0])
                        gradelinee7.setText(chemistry[1])
                        gplinee8.setText(biology[0])
                        gradelinee8.setText(biology[1])
                        gplinee9.setText(bgs[0])
                        gradelinee9.setText(bgs[1])
                        gplinee10.setText(islam[0])
                        gradelinee10.setText(islam[1])
                        gplinee11.setText(physicla[0])
                        gradelinee11.setText(physicla[1])
                        gplinee12.setText(higher_math[0])
                        gradelinee12.setText(higher_math[1])

                        def gpa():
                            banglagp = float(bangla[0])
                            englishgp = float(english[0])
                            mathgp = float(math[0])
                            pysicsgp = float(pysics[0])
                            chemistrygp = float(chemistry[0])
                            biologygp = float(biology[0])
                            bgsgp = float(bgs[0])
                            islamgp = float(islam[0])
                            physicalgp = float(physicla[0])
                            higher_mathgp = float(higher_math[0])
                            if int(writtenlinee12.text()) <= 12 or int(mcqlinee12.text()) <= 11 or int(
                                    practiallinee12.text()) <= 7:
                                higher_mathgplo = float('0.00')
                            else:
                                higher_mathgplo = higher_mathgp - 2.00

                            totalgp = banglagp + englishgp + mathgp + pysicsgp + chemistrygp + \
                                biologygp + bgsgp + islamgp + physicalgp + higher_mathgplo

                            if banglagp == 0.00 or englishgp == 0.00 or mathgp == 0.00 or pysicsgp == 0.00 or chemistrygp == 0.00 or biologygp == 0.00 or bgsgp == 0.00 or islamgp == 0.00 or physicalgp == 0.00 or higher_mathgp == 0.00:
                                gplinee13.setText('0.00')
                                gradelinee13.setText('F')

                            else:

                                v = str(float(totalgp / 9))[0: 4]

                                if v.__len__() == 3:
                                    v = v.__add__('0')

                                if float(v) >= 1.00 and float(v) < 2.00:
                                    gradelinee13.setText('D')
                                elif float(v) >= 2.00 and float(v) < 3.00:
                                    gradelinee13.setText('C')
                                elif float(v) >= 3.00 and float(v) < 3.50:
                                    gradelinee13.setText('B')
                                elif float(v) >= 3.50 and float(v) < 4.00:
                                    gradelinee13.setText('A-')
                                elif float(v) >= 4.00 and float(v) < 5.00:
                                    gradelinee13.setText('A')
                                if float(v) >= 5.00:
                                    gplinee13.setText('5.00')
                                    gradelinee13.setText('A+')
                                else:
                                    gplinee13.setText(v)
                        Thread(target=lambda: gpa()).start()

                        def j():
                        
                            function.databagesave(name=studentdetailname.text(), 
                                            roll=studentdetailroll.text(),
                                        total=totallinee13.text(),
                                        gpa=gplinee13.text(),
                                        grade=gradelinee13.text())
                        Thread(target=lambda: j()).start()
                Thread(target=lambda: allsub()).start()
                 
            Thread(target=lambda: total()).start()




                                    
                
