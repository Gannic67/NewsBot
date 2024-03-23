import pymysql


connection = pymysql.connect(host='147.45.105.54',
                             user='gen_user',
                             password='mfohmdu%E3$b\k',
                             database='News',
                             port=3306)


# with connection:
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM MOSCOW')
#
#     rows = cursor.fetchall()
#
#     for line in rows:
#         print(line)

def get():
    with connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM MOSCOW')

        rows = cursor.fetchall()
        a =''
        for line in rows:
            a += f'{line[1]}\n, {line[2]}\n, {line[3]}\n'
        return a


def smol():
    with connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Smolensk')

        rows = cursor.fetchall()
        b = ''
        for line in rows:
            b += f'{line[1]}\n, {line[2]}\n, {line[3]}\n'
        return b


