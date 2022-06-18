from PyQt5 import QtCore, QtGui, QtWidgets
from handler.Hosp_DB import *


class NewThread(QtCore.QThread):  # вызов в отдельном потоке
    new_signal = QtCore.pyqtSignal(str)  # сигнал, который передаёт строку

    def thread_login(self, snils, password):
        login(snils, password, self.new_signal)  # реализован в бд тест

    def thread_register(self, data):  # так же
        register(data, self.new_signal)

    def register_error(self):
        reg_er(self.new_signal)

    def snils_error(self):
        snils_er(self.new_signal)

    def name_error(self):
        name_er(self.new_signal)

    def mail_error(self):
        mail_er(self.new_signal)

    def phone_error(self):
        phone_er(self.new_signal)
