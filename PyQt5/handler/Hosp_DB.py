import sqlite3  # pip install sqlite3


def login(snils, password, signal):
    bd = sqlite3.connect('C:\\Users\\Коптутер\\PycharmProjects\\Hospital\\handler\\Hospital_DB.sqlite')  # подключаемся к базе данных
    cur = bd.cursor()  # курсор производит действия внутри базы

    cur.execute(f'select snils, password from patients where snils = "{snils}";')  # проверка есть ли аткой пользователь
    value = cur.fetchall()  # результат срочки вышe

    if value != [] and str(value[0][1]) == password:
        signal.emit("Successful Authorization!")  # сигнал попадает в self.check_bd.mysignal.connect(self.signal_handler)
    else:
        signal.emit("Check the validity of the input")

    cur.close()
    bd.close()


def register(data, signal):

    bd = sqlite3.connect('C:\\Users\\Коптутер\\PycharmProjects\\Hospital\\handler\\Hospital_DB.sqlite')
    cur = bd.cursor()

    cur.execute(f'select snils from patients where snils = "{data[0]}";')  # проверка есть ли аткой пользователь
    value = cur.fetchall()
    if value:
        k = 1
    else:
        k = 0

    if k:
        signal.emit("This SNILS is already existed!")
    else:
        y = str(data[4])
        y = y[6:] + "-" + y[3:5] + "-" + y[:2]
        cur.execute(f'insert into patients values ("{int(data[0])}","{str(data[1])}","{str(data[2])}","{str(data[3])}","{y}","{str(data[5])}","{int(data[6])}","{str(data[7])}")')
        signal.emit("You have successfully sign up!")
        bd.commit()  # обновление базы

    cur.close()
    bd.close()


def reg_er(signal):
    signal.emit("Enter all information, please!")


def snils_er(signal):
    signal.emit("All  8 character in snils must be numbers!")


def name_er(signal):
    signal.emit("Name and Surname must not have any symbols!")


def mail_er(signal):
    signal.emit("Your mail must have @ and . in it!")


def phone_er(signal):
    signal.emit("All  11 character in phone number must be numbers!")
