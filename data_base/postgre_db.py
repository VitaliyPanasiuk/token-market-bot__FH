import imp
import sqlite3 as sq
from misc.func import get_balance
from config import DB_URI
import psycopg2


# start bd/ connect and create if does'nt exists
def sql_start_products():
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    if base:
        print('data base users connect Ok!')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users(id serial primary key ,userid text, name TEXT, balance integer, cart integer)')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS stats(id serial primary key , source TEXT, time TEXT, userid TEXT)')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS donate(id serial primary key , userid TEXT, time TEXT, sum TEXT)')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS texts(id serial primary key , name TEXT, description TEXT)')
    base.commit()
    cur.close()
    base.close()


# функция записи в базу данных покупки токена
async def sql_add_transaction(data):
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    cur.execute(
        'INSERT INTO stats (source,time,userid)  VALUES (%s,%s,%s)', data)
    base.commit()
    cur.close()
    base.close()

# функция записи в базу данных пополнения баланса


async def sql_add_donate(data):
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    cur.execute('INSERT INTO donate (userid,time,sum)  VALUES (%s,%s,%s)', data)
    base.commit()
    cur.close()
    base.close()

# функция изменения контекста в перменных сообщений


async def sql_change_texts(name, description):
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    data = (description, name)
    cur.execute('UPDATE texts set description = %s where name = %s', data)
    base.commit()
    cur.close()
    base.close()

# функция регистрации пользователя в системе


async def sql_add_user(data):
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    cur.execute(
        'INSERT INTO users (userid, name, balance, cart)  VALUES (%s,%s,%s,%s)', data)
    base.commit()
    cur.close()
    base.close()

# функции увелисения и уменьшения баланса соотвественно


async def sql_increase_balance(donate, userid):
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    users = cur.execute('SELECT * FROM users').fetchall()
    balance = get_balance(userid)
    balance = int(balance) + int(donate)
    data = (balance, userid)
    cur.execute('UPDATE users set balance = %s where userID = %s', data)
    base.commit()
    cur.close()
    base.close()


async def sql_decrease_balance(donate, userid):
    base = psycopg2.connect(DB_URI, sslmode="require")
    cur = base.cursor()
    users = cur.execute('SELECT * FROM users').fetchall()
    balance = get_balance(userid)
    balance = int(balance) - int(donate)
    data = (balance, userid)
    cur.execute('UPDATE users set balance = %s where userID = %s', data)
    base.commit()
    cur.close()
    base.close()
