from data_base import sqlite_db_users
from config import admins

# функция проверки на доступ к админ функциям
def isAdmin(userid):
    if userid in admins:
        return True
    else:
        return False

# проверкапользоветеля в баще данных
def chek_auf_user(userid):
    users = sqlite_db_users.cur.execute('SELECT * FROM users').fetchall()
    answer = False
    for i in users:
        if str(userid) == str(i[1]):
            answer = True
    
    return answer

# получение фсей информации о профиле
def get_profile(userid):
    users = sqlite_db_users.cur.execute('SELECT * FROM users').fetchall()
    answer = 'профиль не найден'
    for user in users:
        if str(userid) == str(user[1]):
            answer = f"Имя: {user[2]}\nВаш id: {user[1]}\nНа вашем балансе: {user[3]}\nВы совершили покупок: {user[4]}"
    
    return answer

# получение знаеченя баланса пользователя
def get_balance(userid):
    users = sqlite_db_users.cur.execute('SELECT * FROM users').fetchall()
    answer = 'профиль не найден'
    for user in users:
        if str(userid) == str(user[1]):
            answer = user[3]
    return answer