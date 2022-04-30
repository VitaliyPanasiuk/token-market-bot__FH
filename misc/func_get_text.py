from data_base import sqlite_db_users

'''
получение текста переменной
    переменные в базе данных
        - Приветсвенное сообщение on_startup
        - Инструкции instruction
        - Контакты contacts
        - цены на токены 1-3  price_first, price_second, price_third
'''

def get_text(name):
    texts = sqlite_db_users.cur.execute('SELECT * FROM texts').fetchall()
    answer = 'not found'
    for text in texts:
        if text[1] == name:
            answer = text[2]
    
    return answer

