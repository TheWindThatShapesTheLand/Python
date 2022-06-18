import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets  # pip install pyqt5
from Check_DB import *
from Inter import *  # pyuic5 name.ui -o inter.py
from Registr import *
from Info import *
import sqlite3


class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.init()
        self.check = NewThread()  # создаём эксземпляр класса
        self.check.new_signal.connect(self.signal_handler)

    def init(self):
        self.ui = Ui_Initialization()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.auth)  # точно так же
        self.ui.pushButton.clicked.connect(self.reg)

    def reg(self):
        self.ui = Ui_Registartion()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.init)
        self.ui.pushButton.clicked.connect(self.new_patient)

    def info(self):
        snils = self.ui.lineEdit.text()
        self.ui = Ui_Info()
        self.ui.setupUi(self)

        patient_data = self.bd_search_id(snils)
        appoint_data = self.bd_search_appoint(snils)
        self.ui.textEdit.setText(f"Hello,{patient_data}!\n\n\n\n\n\n\n\n\tYour appointments:")

        for i in range(len(appoint_data)):
            self.ui.textEdit_2.append(str(appoint_data[i][0]) + ' ' + str(appoint_data[i][1]) + ' ' + str(appoint_data[i][2]) + ' ' + str(appoint_data[i][3]))

        self.ui.pushButton.clicked.connect(self.init)

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, "Notification", value)

        if value == "Successful Authorization!":
            self.info()

    def auth(self):
        snils = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.check.thread_login(snils, password)  # выполнит метод из другого файла, возьмёт логин и пароль

    def new_patient(self):
        snils = self.ui.lineEdit.text()
        name = self.ui.lineEdit_2.text()
        surname = self.ui.lineEdit_3.text()
        if self.ui.radioButton.isChecked() is False and self.ui.radioButton_2.isChecked() is False:
            self.check.register_error()
            return
        elif self.ui.radioButton.isChecked() is not False and self.ui.radioButton_2.isChecked() is False:
            sex = "Male"
        else:
            sex = "Female"
        birthday = self.ui.dateEdit.text()
        mail = self.ui.lineEdit_4.text()
        phone_number = self.ui.lineEdit_5.text()
        password = self.ui.lineEdit_6.text()

        data = [snils, name, surname, sex, birthday, mail, phone_number, password]

        for i in range(len(data)):
            if data[i] == "":
                self.check.register_error()
                return
            else:
                if i == 1:
                    if snils.isnumeric() is False or len(str(snils)) != 8:
                        self.check.snils_error()
                        return
                if i == 2:
                    if name.isalpha() is False:
                        self.check.name_error()
                        return
                if i == 3:
                    if surname.isalpha() is False:
                        self.check.name_error()
                        return
                if i == 6:
                    if ('@' or '.') not in mail:
                        self.check.mail_error()
                        return
                if i == 7:
                    if phone_number.isnumeric() is False or len(str(phone_number)) != 11:
                        self.check.phone_error()
                        return

        self.check.thread_register(data)

    def bd_search_id(self, snils):
        bd = sqlite3.connect('C:\\Users\\Коптутер\\PycharmProjects\\Hospital\\handler\\Hospital_DB.sqlite')  # подключаемся к базе данных
        cur = bd.cursor()

        cur.execute(f'select name, surname from patients where snils = "{snils}";')  # проверка есть ли аткой пользователь
        value = cur.fetchall()

        return value[0][0] + " " + value[0][1]

    def bd_search_appoint(self, snils):
        bd = sqlite3.connect(
            'C:\\Users\\Коптутер\\PycharmProjects\\Hospital\\handler\\Hospital_DB.sqlite')  # подключаемся к базе данных
        cur = bd.cursor()

        cur.execute(f'select doctor, day_, time_, cabinet from Appointments a inner join Patients p on p.SNILS  = a.patients_snils where p.SNILS = {snils};')
        value = cur.fetchall()
        new_value = []

        for i in range(len(value)):
            new_value += [value[i]]

        return new_value


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()

    sys.exit(app.exec_())
