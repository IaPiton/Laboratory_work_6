import sqlite3
from flask import Flask, render_template, request

conn = sqlite3.connect('gifts.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS gifts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    gift TEXT,
    cost REAL,
    status TEXT
)
''')

gifts = [
    ('Иван Иванович', 'Санки', 2000.00, 'куплен'),
    ('Ирина Сергеевна', 'Цветы', 3000.00, 'не куплен'),
    ('Петр Петрович', 'Книга', 1500.00, 'не куплен'),
    ('Анна Анovna', 'Теремок', 1000.00, 'не куплен'),
    ('Михаил Михайлович', 'Ботинки', 2500.00, 'не куплен'),
    ('Елена Егорова', 'Софт-толикон', 500.00, 'не куплен'),
    ('Владимир Владимирович', 'Реплика', 800.00, 'не куплен'),
    ('Ольга Олеговна', 'Фотоаппарат', 3000.00, 'не куплен'),
    ('Алексей Алексеевич', 'Кофемашина', 2500.00, 'не куплен'),
    ('Николай Николаевич', 'Быстроход', 4000.00, 'не куплен')
]

sql_query = '''
INSERT INTO gifts (name, gift, cost, status)
VALUES (?, ?, ?, ?)
'''
cursor.execute('DELETE FROM gifts')
for gift in gifts:
    cursor.execute(sql_query, gift)

conn.commit()
conn.close()
print("Данные успешно добавлены в базу данных.")

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('gifts.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    gifts = conn.execute('SELECT * FROM gifts').fetchall()
    conn.close()
    return render_template('index.html', gifts=gifts)

if __name__ == '__main__':
    app.run(debug=True)

