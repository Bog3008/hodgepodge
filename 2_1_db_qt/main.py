import psycopg2
from psycopg2 import Error
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

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



class AnotherWindow(QTableWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, text):
        super().__init__()
        #if
        print(text)
        collumn = ""
        if text == "sort by Date":
            collumn = "date"
        if text == "sort by tg_id":
            collumn = "tg_id"
        if text == "sort by Date DESC":
            collumn = "date DESC"
        querry1 = select_from_message_order(collumn)

        #end_if
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

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.

        x_size = 500
        y_size = 500
        self.setGeometry(x_size, y_size, x_size, y_size)
        self.setWindowTitle("CodersLegacy")

        combo = QtWidgets.QComboBox(self)
        combo.addItems(["sort by Date", "sort by Date DESC" , "sort by tg_id"])
        combo.move(10, 10)
        combo.setGeometry(200, 150, 200, 50)
        combo.activated[str].connect(self.show_new_window)
        '''button = QtWidgets.QPushButton(self)
        button.setText("Submit")
        table = QTableWidget()
        button.clicked.connect(self.show_new_window)
        button.move(200, 10)'''
        '''self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)'''

    def show_new_window(self, text):
        #print(text)
        if self.w is None:
            self.w = AnotherWindow(text)
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
#insert_into_message(3, "message № 2")
#select_from_tg_user()
#select_from_message()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
