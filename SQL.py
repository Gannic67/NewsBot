"""
Подключение к базе данных
"""


import pymysql
import os

connection = pymysql.connect(host=os.getenv('BD_HOST'),
                             user='BD_USER',
                             password=os.getenv('BD_PASSWORD'),
                             database='News',
                             port='BD_PORT')