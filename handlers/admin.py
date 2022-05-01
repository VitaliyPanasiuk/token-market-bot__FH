import os
from pydoc import describe
from config import dp, bot,admins
from keyboards import inline_key as kb
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import sqlite3 as sq
from data_base import sqlite_db_users
from aiogram.types import Message, ReplyKeyboardMarkup
from misc.func import isAdmin
from misc.func_get_text import get_text
from states.change_text_state import changetext

from datetime import datetime

class FSMAdd(StatesGroup):
    name = State()
    description = State()
    category = State()
    img = State()


# ИЗМЕНЕНИЕ ТЕКСТОВ ТАКИХ ПЕРЕМЕННЫХ КАК ПРИВЕТСВИЕ,ИНСТРУКЦИИ,КОНТАКТЫ,ЦЕНА1-3
async def change_texts_command(message: types.Message):
    userid = message.from_user.id
    if isAdmin(userid):
        await bot.send_message(userid,'Выберите что вы хотите изменить',reply_markup=kb.inline_kb_change_text)

# CHANGE ON_STARTUP TEXT
# @dp.callback_query_handler(lambda c: c.data == 'on_startup')
async def on_startup_button(callback_query: types.CallbackQuery, state=changetext):
    await bot.send_message(callback_query.from_user.id,'Текущий текст\n' + get_text('on_startup') )
    await bot.send_message(callback_query.from_user.id,'Ведите новый текст: ' )
    async with state.proxy() as data:
        data['name'] = 'on_startup'
    await changetext.get_description.set()
    

# CHANGE INSTRUCTION TEXT
# @dp.callback_query_handler(lambda c: c.data == 'instruction')
async def instruction_button(callback_query: types.CallbackQuery, state=changetext):
    await bot.send_message(callback_query.from_user.id,'Текущий текст\n' + get_text('instruction') )
    await bot.send_message(callback_query.from_user.id,'Ведите новый текст: ' )
    async with state.proxy() as data:
        data['name'] = 'instruction'
    await changetext.get_description.set()

# CHANGE CINTACTS TEXT
# @dp.callback_query_handler(lambda c: c.data == 'contacts')
async def contacts_button(callback_query: types.CallbackQuery, state=changetext):
    await bot.send_message(callback_query.from_user.id,'Текущий текст\n' + get_text('contacts') )
    await bot.send_message(callback_query.from_user.id,'Ведите новый текст: ' )
    async with state.proxy() as data:
        data['name'] = 'contacts'
    await changetext.get_description.set()

# CHANGE PRICE1 TEXT
# @dp.callback_query_handler(lambda c: c.data == 'price1')
async def price1_button(callback_query: types.CallbackQuery, state=changetext):
    await bot.send_message(callback_query.from_user.id,'Текущий текст\n' + get_text('price_first') )
    await bot.send_message(callback_query.from_user.id,'Ведите новый текст: ' )
    async with state.proxy() as data:
        data['name'] = 'price_first'
    await changetext.get_description.set()

# CHANGE PRICE2 TEXT
# @dp.callback_query_handler(lambda c: c.data == 'price2')
async def price2_button(callback_query: types.CallbackQuery, state=changetext):
    await bot.send_message(callback_query.from_user.id,'Текущий текст\n' + get_text('price_second') )
    await bot.send_message(callback_query.from_user.id,'Ведите новый текст: ' )
    async with state.proxy() as data:
        data['name'] = 'price_second'
    await changetext.get_description.set()

# CHANGE PRICE3 TEXT
# @dp.callback_query_handler(lambda c: c.data == 'price3')
async def price3_button(callback_query: types.CallbackQuery, state=changetext):
    await bot.send_message(callback_query.from_user.id,'Текущий текст\n' + get_text('price_third') )
    await bot.send_message(callback_query.from_user.id,'Ведите новый текст: ' )
    async with state.proxy() as data:
        data['name'] = 'price_third'
    await changetext.get_description.set()

# ВНЕСЕНИЕ ИЗМЕНЕНИЙ В БАЗУ ДАННЫХ
async def get_change_text(message, state=changetext.get_description):
    async with state.proxy() as data:
        data['get_description'] = message.text
    await sqlite_db_users.sql_change_texts(data['name'],data['get_description'])
    await state.finish()

#  ПОЛУЧАЕМ СТАТИСТИКУ БОТА ЗА ТЕКУЩИЙ ДЕНЬ 
async def get_stats_command(message, state=changetext.get_description):
    userid = message.from_user.id
    today = datetime.now().strftime('%d.%m.%Y')
    sum_of_donate = 0
    amount_of_get_token = 0
    amount_of_users = 0

    stats = sqlite_db_users.cur.execute('SELECT * FROM stats').fetchall()
    for stat in stats:
        if str(stat[2]) == str(today):
            amount_of_get_token += 1

    transaction = sqlite_db_users.cur.execute('SELECT * FROM donate').fetchall()
    for trans in stats:
        if str(trans[2]) == str(today):
            sum_of_donate += trans[3]

    users = sqlite_db_users.cur.execute('SELECT * FROM users').fetchall()
    for user in users:
        amount_of_users += 1

    await bot.send_message(userid,
        f'Статистика бота за текущий день\nКоличесво пользователей бота: {amount_of_users}\nСумма пополнений: {sum_of_donate}\nКолтчсество покупок токенов: {amount_of_get_token}')





def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(change_texts_command,commands=['changetext'])
    dp.register_message_handler(get_stats_command,commands=['getstats'])

    dp.register_callback_query_handler(on_startup_button, lambda c: c.data == 'on_startup')
    dp.register_callback_query_handler(instruction_button, lambda c: c.data == 'instruction')
    dp.register_callback_query_handler(contacts_button, lambda c: c.data == 'contacts')
    dp.register_callback_query_handler(price1_button, lambda c: c.data == 'price1')
    dp.register_callback_query_handler(price2_button, lambda c: c.data == 'price2')
    dp.register_callback_query_handler(price3_button, lambda c: c.data == 'price3')
    dp.register_message_handler(get_change_text,state=changetext.get_description)



    

    
