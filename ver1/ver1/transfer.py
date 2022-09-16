import sqlite3
import time
import psycopg2
import os

conn_p = psycopg2.connect(dbname='postgres', user='postgres',
                          password='12345678', host='localhost')
cursor_p = conn_p.cursor()

# print(cursor_p.execute('''SELECT * FROM news_news'''))


conn_s = sqlite3.connect('C:\\Users\\vivat\\PycharmProjects\\DJ_with_PG\\ver1\db.sqlite3')
cursor_s = conn_s.cursor()

cat = cursor_s.execute('''SELECT * FROM news_category''').fetchall()

print(cat)
for i in cat:
    cursor_p.execute(
        f'''INSERT INTO news_category (title) VALUES
        ('{i[1]}')''')
conn_p.commit()







a = cursor_s.execute('''SELECT * FROM news_news''').fetchall()
new_list = []
main_list = []
for i in a:
    for e in i:
        if type(e) == str and '\'' in e:
            e = e.replace('\'', '`')
        new_list.append(e)
    main_list.append(new_list)
    new_list = []

for i in main_list:
    print({i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}, {i[6]}, {i[7]})
    cursor_p.execute(
        f'''INSERT INTO news_news (title,content,created_at,update_at,photo,category_id,is_published) VALUES
        ('{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}')''')
conn_p.commit()




