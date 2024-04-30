"""
Подключение к базе данных
"""


import pymysql
import os

connection = pymysql.connect(host=os.getenv('BD_HOST'),
                             user='gen_user',
                             password=os.getenv('BD_PASSWORD'),
                             database='News',
                             port=3306)