import pymysql


connection = pymysql.connect(host='147.45.105.54',
                             user='gen_user',
                             password='mfohmdu%E3$b\k',
                             database='News',
                             port=3306)


with connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Smolensk')

    rows = cursor.fetchall()

    for line in rows:
        print(line)

