from SQL import connection

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

def getsmoscow():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mascowDTP')
    rows = cursor.fetchall()
    q =[]
    for line in rows:
        q.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return q


def smol():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Smolensk')
    rows = cursor.fetchall()
    b = []
    for line in rows:
        b.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return b

def smols():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM SmolenskDTP')
    rows = cursor.fetchall()
    q = []
    for line in rows:
        q.append(f'{line[1]}\n\n, {line[2]}\n\n, {line[3]}\n\n')
    return q






