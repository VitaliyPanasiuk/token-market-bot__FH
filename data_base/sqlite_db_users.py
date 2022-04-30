import sqlite3 as sq
from misc.func import get_balance


# start bd/ connect and create if does'nt exists
def sql_start_products():
    global base, cur
    base = sq.connect('tg-getToken.db')
    cur = base.cursor()
    if base:
        print('data base users connect Ok!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,userid INT, name TEXT, balance INT, cart INT)')
    base.execute('CREATE TABLE IF NOT EXISTS stats(id INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT, time TEXT, userid TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS donate(id INTEGER PRIMARY KEY AUTOINCREMENT, userid TEXT, time TEXT, sum TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS texts(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)')
    base.commit()

# функция записи в базу данных покупки токена
async def sql_add_transaction(data):
    cur.execute('INSERT INTO stats (source,time,userid)  VALUES (?,?,?)', data)
    base.commit()

# функция записи в базу данных пополнения баланса
async def sql_add_donate(data):
    cur.execute('INSERT INTO donate (userid,time,sum)  VALUES (?,?,?)', data)
    base.commit()

# функция изменения контекста в перменных сообщений
async def sql_change_texts(name,description):
    data = (description,name)
    cur.execute('UPDATE texts set description = ? where name = ?', data)
    base.commit()

# функция регистрации пользователя в системе
async def sql_add_user(data):
    cur.execute('INSERT INTO users (userid,name,balance,cart)  VALUES (?,?,?,?)', data)
    base.commit()

# функции увелисения и уменьшения баланса соотвественно
async def sql_increase_balance(donate,userid):
    users = cur.execute('SELECT * FROM users').fetchall()
    balance = get_balance(userid)
    balance = int(balance) + int(donate)
    data = (balance,userid)
    cur.execute('UPDATE users set balance = ? where userID = ?', data)
    base.commit()

async def sql_decrease_balance(donate,userid):
    users = cur.execute('SELECT * FROM users').fetchall()
    balance = get_balance(userid)
    balance = int(balance) - int(donate)
    data = (balance,userid)
    cur.execute('UPDATE users set balance = ? where userID = ?', data)
    base.commit()


