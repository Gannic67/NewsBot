"""
Модуль работы с базой данных где представлены запросы выбора новостей по городам
"""

from SQL import connection


def moscow_generalnews():
    """
    Функция вывода новостей Москва из таблицы построчно
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM MOSCOW')
    rows = cursor.fetchall()
    news_moscow =[]
    for line in rows:
        news_moscow.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return news_moscow

def news_moscow():
    """
    Функция вывода новостей Москва из таблицы построчно
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mascowDTP')
    rows = cursor.fetchall()
    news_moscow =[]
    for line in rows:
        news_moscow.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return news_moscow


def smol_news():
    """
    Функция вывода новостей Смоленск из таблицы построчно
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Smolensk')
    rows = cursor.fetchall()
    news_smolensk = []
    for line in rows:
        news_smolensk.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return news_smolensk

def smol_dtp():
    """
    Функция вывода новостей Смоленск из таблицы построчно
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM SmolenskDTP')
    rows = cursor.fetchall()
    news_smolensk = []
    for line in rows:
        news_smolensk.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return news_smolensk






