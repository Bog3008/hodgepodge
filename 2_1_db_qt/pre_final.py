import psycopg2
from psycopg2 import Error
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QMessageBox, QLineEdit
import re
def create_user_table():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="3008",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test")

        # Создайте курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # SQL-запрос для создания новой таблицы
        create_table_query = '''CREATE TABLE tg_user(
                                             user_id SERIAL PRIMARY KEY ,
                                             tg_id           TEXT    NOT NULL,
                                             name TEXT,
                                             UNIQUE (tg_id)
                                             ); '''
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица успешно создана в PostgreSQL")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

def create_message_table():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="3008",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test")

        # Создайте курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # SQL-запрос для создания новой таблицы
        create_table_query = '''CREATE TABLE message(
                                             message_id SERIAL PRIMARY KEY ,
                                             user_id           INT,
                                             message TEXT,
                                             date timestamp,
                                             FOREIGN KEY (user_id)  REFERENCES tg_user (user_id) ON DELETE SET NULL
                                             ); '''
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица сообщений успешно создана в PostgreSQL")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

def insert_into_tg_user(nik_name, real_name):
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
        insert_query = """ INSERT INTO  tg_user(tg_id, name) 
                           VALUES (%s, %s)
                           """
        insert_args = (nik_name, real_name)
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

def insert_into_message(user_id, message):
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
                           VALUES (%s, %s, NOW())
                           """
        insert_args = (user_id, message)
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

def select_from_tg_user():
    import psycopg2
    import datetime
    from psycopg2 import Error

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
        cursor.execute("SELECT * FROM tg_user")
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
            SELECT tg_id,
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

def select_from_message_order(collumn):

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
            SELECT tg_id,
                   name,
                   message,
                   date
            FROM message JOIN tg_user USING(user_id)
            ORDER BY ''' + collumn
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

def select_tg_id():

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
            SELECT 
                DISTINCT tg_id
            FROM tg_user
            ORDER BY tg_id
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

def execute_querry(querry):

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

class AnotherWindow(QTableWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, param):
        super().__init__()
        #if
        print(param)
        querry = '''
                    SELECT tg_id,
                           name,
                           message,
                           date
                    FROM message JOIN tg_user USING(user_id)
                    '''
        if not((param[2] == "all_names")):
            querry += "\nWHERE tg_id LIKE \'_" + param[2][1:] + "\'"
###timechek &&&
            if not(param[3] == '0000-00-00'):
                '''querry += "AND DATEDIFF(date,"+param[3] + ") > 0"'''
                querry += " AND EXTRACT(day from date - \'" + param[3] + "\'::timestamp) > 0"
        elif(not(param[3] == '0000-00-00')):
            querry += "WHERE EXTRACT(day from date - '%s'::timestamp) > 0" % param[3]
        querry += "\nORDER BY " + param[0] + " " + param[1]
        print(querry)

        querry1 = execute_querry(querry)

        #end_if
        row_l = 0
        col_l = 0
        if len(querry1) != 0:
            row_l = len(querry1)
            col_l = len(querry1[0])
            print(col_l, row_l)
            #table = QTableWidget()  # Create a table
            self.horizontalHeader().setVisible(True)
            self.horizontalHeader().setCascadingSectionResizes(True)
            self.horizontalHeader().setDefaultSectionSize(140)
            self.horizontalHeader().setHighlightSections(False)
            self.horizontalHeader().setMinimumSectionSize(100)
            self.horizontalHeader().setSortIndicatorShown(False)
            self.horizontalHeader().setStretchLastSection(False)

            self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.setMinimumSize(QSize(1000, 1000))
            self.setColumnCount(col_l)  # Set three columns
            self.setRowCount(row_l)
            self.setHorizontalHeaderLabels(["Telegram id", "Name", "message", "Date"])
            for i in range(col_l):
                for j in range(row_l):
                    self.setItem(j, i, QTableWidgetItem(str(querry1[j][i])))
        else:
            self.label_1 = QLabel('no results', self)
            self.label_1.setGeometry(0, 0, 350, 50)


class MainWindow(QMainWindow):
    param = ["date", "ASC", "all_names", "null_date"]
    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.

        x_size = 1200
        y_size = 700
        self.setGeometry(x_size, y_size, x_size, y_size)
        self.setWindowTitle("CodersLegacy")
### SORT ###
        x_pos, y_pos = 10, 10
        combo = QtWidgets.QComboBox(self)
        combo.addItems(["date", "name", "tg_id"])
        combo.move(10, 10)
        combo.setGeometry(x_pos, y_pos, 200, 50)
        combo.activated[str].connect(self.set_sort)

        self.label_1 = QLabel('Main sort parametr', self)
        self.label_1.setGeometry(x_pos + 250, y_pos, 350, 50)
## ASC & DESC ###
        y_pos = y_pos + 100
        combo05 = QtWidgets.QComboBox(self)
        combo05.addItems(["ASC", "DESC"])
        combo05.move(10, 10)
        combo05.setGeometry(x_pos, y_pos, 200, 50)
        combo05.activated[str].connect(self.set_order)
        self.label_1 = QLabel('Order parametr', self)
        self.label_1.setGeometry(x_pos+250, y_pos, 350, 50)
### NAME SELECTION ###
        y_pos = y_pos + 100
        comb2_q = select_tg_id()
        list_tg_ig = list()
        list_tg_ig.append("all_names")
        for i in range(len(comb2_q)):
            list_tg_ig.append(comb2_q[i][0])
        combo2 = QtWidgets.QComboBox(self)
        combo2.addItems(list_tg_ig)
        combo2.move(10, 10)
        combo2.setGeometry(x_pos, y_pos, 200, 50)
        combo2.activated[str].connect(self.set_name)

        self.label_1 = QLabel('Show user with this name', self)
        self.label_1.setGeometry(x_pos+250, y_pos, 350, 50)

### TXT INPUT###
        y_pos = y_pos + 100
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 10)
        self.textbox.setGeometry(x_pos, y_pos, 200, 50)
        self.textbox.setInputMask("0000-00-00")
        self.textbox.setText("0000-00-00")
        #self.textbox.resize(280, 40)
        self.label = QLabel('Date from (date format: \'YYYY-MM-DD\'); \n"0000-00-00" - all dates', self)
        self.label.setGeometry(x_pos + 250, y_pos, 700, 50)

        '''self.label2 = QLabel('This is label 2', self)
        self.label2.setGeometry(100, 150, 100, 100)'''
### button ###
        y_pos = y_pos + 100
        button = QPushButton('Show result table', self)
        button.setToolTip('This is an example button')
        button.setGeometry(x_pos, y_pos, 200, 100)
        button.clicked.connect(self.on_click)

        '''button = QtWidgets.QPushButton(self)
        button.setText("Submit")
        table = QTableWidget()
        button.clicked.connect(self.show_new_window)
        button.move(200, 10)'''
        '''self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)'''

    def on_click(self):
        textboxValue = self.textbox.text()
        if(not(re.search("[0-9]{4}[-]{1}[0-9]{2}[-]{1}[0-9]{2}",textboxValue))):
            print("not ok text value")
            QMessageBox.about(self, "ERROR", "incorrect date")
            return
        self.param[3] = textboxValue
        print(self.param)
        self.show_new_window()

## func for text_boxes ##
    def set_sort(self, text):
        self.param[0] = text
    def set_order(self, text):
        self.param[1] = text
    def set_name(self, text):
        self.param[2] = text


    def show_new_window(self):
        if self.w is None:
            self.w = AnotherWindow(self.param)
            self.w.show()

        else:
            self.w.close()  # Close window.
            self.w = None  # Discard reference.





#create_user_table()
#create_message_table()
#insert_into_tg_user("@bog", "Bogdan")
#insert_into_tg_user("@and", "Andrew")
#insert_into_tg_user("@mike", "Mike Vazovski")
#insert_into_message(1, "hi!")
#insert_into_message(3, "idk (№ 4)")
#insert_into_message(1, "QWERY (№ 5)")
#select_from_tg_user()
#select_from_message()
#insert_into_message(3, "Aba (mess №3)")
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
