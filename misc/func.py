from data_base import postgre_db
from config import admins

from config import DB_URI
import psycopg2

# функция проверки на доступ к админ функциям


def isAdmin(userid):
    if userid in admins:
        return True
    else:
        return False

# проверкапользоветеля в баще данных


def chek_auf_user(userid):
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    answer = False
    for i in users:
        if str(userid) == str(i[1]):
            answer = True
    cur.close()
    base.close()

    return answer

# получение фсей информации о профиле


def get_profile(userid):
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    answer = 'профиль не найден'
    for user in users:
        if str(userid) == str(user[1]):
            answer = f"Имя: {user[2]}\nВаш id: {user[1]}\nНа вашем балансе: {user[3]}\nВы совершили покупок: {user[4]}"

    cur.close()
    base.close()
    return answer

# получение знаеченя баланса пользователя


def get_balance(userid):
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    answer = 'профиль не найден'
    for user in users:
        if str(userid) == str(user[1]):
            answer = user[3]

    cur.close()
    base.close()
    return answer
