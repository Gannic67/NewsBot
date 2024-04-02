import pymysql


connection = pymysql.connect(host='147.45.105.54',
                             user='gen_user',
                             password='|2?xzWwGa+KF\B',
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

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM MOSCOW')

    rows = cursor.fetchall()
    a =[]
    for line in rows:
        a.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return a


def smol():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Smolensk')

    rows = cursor.fetchall()
    b = []
    for line in rows:
        b.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return b


