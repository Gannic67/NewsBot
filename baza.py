from SQL import connection


def get():
    """
    Функция вывода новостей Москва из таблицы построчно
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM MOSCOW')
    rows = cursor.fetchall()
    News_Moscow =[]
    for line in rows:
        News_Moscow.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return News_Moscow

def getsmoscow():
    """
    Функция вывода новостей Москва из таблицы построчно
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mascowDTP')
    rows = cursor.fetchall()
    News_Moscow =[]
    for line in rows:
        News_Moscow.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return News_Moscow


def smol():
    """
    Функция вывода новостей Смоленск из таблицы построчно
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Smolensk')
    rows = cursor.fetchall()
    News_Smolensk = []
    for line in rows:
        News_Smolensk.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return News_Smolensk

def smols():
    """
    Функция вывода новостей Смоленск из таблицы построчно
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM SmolenskDTP')
    rows = cursor.fetchall()
    News_Smolensk = []
    for line in rows:
        News_Smolensk.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return News_Smolensk






