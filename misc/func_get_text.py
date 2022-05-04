from data_base import postgre_db

from config import DB_URI
import psycopg2

'''
получение текста переменной
    переменные в базе данных
        - Приветсвенное сообщение on_startup
        - Инструкции instruction
        - Контакты contacts
        - цены на токены 1-3  price_first, price_second, price_third
'''


def get_text(name):
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    cur.execute('SELECT * FROM texts')
    texts = cur.fetchall()
    answer = 'not found'
    for text in texts:
        if text[1] == name:
            answer = text[2]

    cur.close()
    base.close()
    return answer
