import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView, QAbstractItemView, QPushButton, QTableWidget, \
                            QTableWidgetItem, QVBoxLayout, QHBoxLayout, QStyledItemDelegate, QMessageBox
from PyQt5.QtCore import Qt

import psycopg2
from psycopg2 import Error


def select_from_message():

    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="3008",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test")
        cursor = connection.cursor()
        # Выполнение SQL-запроса для вставки даты и времени в таблицу


        # Считать значение времени покупки PostgreSQL в Python datetime
        querry = '''
            SELECT message_id,
                   user_id,
                   tg_id,
                   name,
                   message,
                   date
            FROM message JOIN tg_user USING(user_id)
        '''
        cursor.execute(querry)
        tg_user_id_list = cursor.fetchall()
        print(tg_user_id_list)
        return tg_user_id_list
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
def insert_into_message(user_id, message, date = "NOW()"):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="3008",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test")

        cursor = connection.cursor()
        # Выполнение SQL-запроса для вставки данных в таблицу
        insert_query = """ INSERT INTO  message(user_id, message, date) 
                           VALUES (%s, %s, %s)
                           """
        insert_args = (user_id, message, date)
        cursor.execute(insert_query, insert_args)
        connection.commit()
        print( insert_args, "успешно вставлены")


    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
def execute_querry(querry):

    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="3008",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test")
        connection.autocommit = True
        cursor = connection.cursor()
        # Выполнение SQL-запроса для вставки даты и времени в таблицу


        # Считать значение времени покупки PostgreSQL в Python datetime

        cursor.execute(querry)
        tg_user_id_list = cursor.fetchall()
        print(tg_user_id_list)
        return tg_user_id_list
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
class TableWidget(QTableWidget):
    q_res = select_from_message()
    def __init__(self):
        super().__init__(1, 6)
        self.setHorizontalHeaderLabels(["m_id","user_id","Telegram id", "Name", "message", "Date"])
        self.verticalHeader().setDefaultSectionSize(50)
        self.horizontalHeader().setDefaultSectionSize(250)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount )
#NEW FIXED
    def _removeRow(self):
        if self.rowCount() != len(self.q_res):
            QMessageBox.about(self, "Error", "delete unsaved row")
            return
        if self.rowCount() > 0:
            self.removeRow(self.currentRow())

        q_r = self.q_res[self.currentRow()+1]
        print("current querry line:", q_r)
        boof = "\'"
        querry = '''
            DELETE FROM message
            WHERE message_id = ''' + boof + str(q_r[0]) + boof


        print(querry)
        execute_querry(querry) #FIXEd #
    def _copyRow(self):
        if self.rowCount() != len(self.q_res):
            QMessageBox.about(self, "Error", "U cant copy unsaved row")
            return
        self.insertRow(self.rowCount())
        rowCount = self.rowCount()
        columnCount = self.columnCount()
        row_content = list()

        print(self.currentRow())
        q_r = self.q_res[self.currentRow()]
        print("current querry line:", q_r)


        for j in range(columnCount):
            if not self.item(self.currentRow(), j) is None:
                self.setItem(rowCount-1, j, QTableWidgetItem(self.item(self.currentRow(), j).text()))
                # row_content.append(self.item(rowCount-2, j).text())
                #row_content.append(self.item(self.currentRow(), j).text())
                row_content.append(self.item(self.currentRow(), j).text())
            else:
                QMessageBox.about(self, "Error", "U have empty cell")
                return
                row_content.append(None)
        insert_into_message(q_r[1],q_r[4], q_r[5])

    def _start(self):
        q_row =len(self.q_res)
        q_col = len(self.q_res[0])
        '''self.insertRow(self.rowCount())
        rowCount = self.rowCount()
        columnCount = self.columnCount()'''
        for i in range(q_row):
            self.insertRow(self.rowCount())
            for j in range(q_col):
                self.setItem(i, j, QTableWidgetItem(str(self.q_res[i][j])))

    def _update(self):
        for i in range(self.rowCount()+1, -1, -1):
            self.removeRow(i)

        self.q_res = select_from_message()
        q_row =len(self.q_res)
        q_col = len(self.q_res[0])
        '''self.insertRow(self.rowCount())
        rowCount = self.rowCount()
        columnCount = self.columnCount()'''
        for i in range(q_row):
            self.insertRow(self.rowCount())
            for j in range(q_col):
                self.setItem(i, j, QTableWidgetItem(str(self.q_res[i][j])))

    def _cfr(self):
        self.removeRow(0)
# EMPTY FIX
# SAVEcurrent
    def _updt(self): #save changes current row
        columnCount = self.columnCount()
        row_content = list()
        curr_r = self.currentRow()
        for j in range(columnCount):
            if not self.item(self.currentRow(), j) is None:
                row_content.append(self.item(self.currentRow(), j).text())
            else:
                row_content.append(None)
        for i in row_content:
            if i == None:
                QMessageBox.about(self, "Error", "U have empty cel")
                return
        print("WWWWWWWW")
        print(row_content)
        print(self.q_res[curr_r])
        if (str(self.q_res[curr_r][0]) != row_content[0]) or (str(self.q_res[curr_r][1]) != row_content[1]) or (str(self.q_res[curr_r][2]) != row_content[2]) or (str(self.q_res[curr_r][3]) != row_content[3]):
            QMessageBox.about(self, "Erro", "U can edit only message and date")
            return
        boof = "\'"
        querry ='''
            UPDATE message
            SET message = ''' +boof+ row_content[4] +boof+ ", date = NOW() " + "WHERE message_id = " + str(self.q_res[curr_r][0])
        #print(querry)
        execute_querry(querry)

    def _saveNew(self):
        columnCount = self.columnCount()
        row_content = list()
        curr_r = self.currentRow()
        for j in range(columnCount):
            if not self.item(self.currentRow(), j) is None:
                row_content.append(self.item(self.currentRow(), j).text())
            else:
                row_content.append(None)
        for i in range(2, len(row_content) - 1):
            if row_content[i] == None:
                QMessageBox.about(self, "Error", "U have empty cel")
                return
        ### INSERT IN TABLES ###
        boof = "\'"
        q_in1 = ''' 
            INSERT INTO tg_user (tg_id, name) VALUES ( ''' +  boof + row_content[2] + boof + "," + boof + row_content[3] + boof + ")"
        print("WWWWWWWW")
        print(q_in1)
        print( execute_querry(q_in1))
        q_in2 = '''
            SELECT user_id
            FROM tg_user
            WHERE tg_id = ''' + boof + row_content[2] + boof
        q_out2 = execute_querry(q_in2)
        print(q_out2)
        q_in3 = '''
        INSERT INTO message (date, user_id, message)
        VALUES (NOW(), ''' + str(q_out2[0][0]) + ", " + boof +  row_content[4] + boof + ")"
        q_out3 = execute_querry(q_in3)
        #print(q_out3)
class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1800, 600)
        mainLayout = QHBoxLayout()
        table = TableWidget()
        mainLayout.addWidget(table)
        buttonLayout = QVBoxLayout()

        button_new = QPushButton('Update')
        button_new.clicked.connect(table._update)
        buttonLayout.addWidget(button_new)

        button_copy = QPushButton('Copy')
        button_copy.clicked.connect(table._copyRow)
        buttonLayout.addWidget(button_copy)

        button_remove = QPushButton('Remove')
        button_remove.clicked.connect(table._removeRow)
        buttonLayout.addWidget(button_remove)

        button_remove = QPushButton('Save current')
        button_remove.clicked.connect(table._updt)
        buttonLayout.addWidget(button_remove, alignment=Qt.AlignTop)

        button_new = QPushButton('New')
        button_new.clicked.connect(table._addRow)
        buttonLayout.addWidget(button_new)
        button_new = QPushButton('Save new')
        button_new.clicked.connect(table._saveNew)
        buttonLayout.addWidget(button_new)

        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
        table._cfr()
        table._start()

app = QApplication(sys.argv)
app.setStyleSheet('QPushButton{font-size: 20px; width: 200px; height: 50px}')
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
