from multiprocessing.connection import answer_challenge
import os
from pydoc import describe
from config import dp, bot,admins
# from keyboards import inline_key as kb
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import sqlite3 as sq
from data_base import sqlite_db_users
from aiogram.types import Message, ReplyKeyboardMarkup
from misc.texts import SERVICE_FIRST, SERVICE_SECOND, SERVICE_THIRD
from misc.func import chek_auf_user, get_profile, get_balance
from misc.func_get_text import get_text
from keyboards.text_key import start_markup, profile_markup,services_markup,cancel_markup

from aiogram.dispatcher.filters.state import State, StatesGroup
from states.donate_state import donateState

from datetime import datetime


# стартовая команда. если пользователя нет в системе вноситься в бд
async def start_command(message: types.Message):
    userid = message.from_user.id
    user_name = message.from_user.username

    if chek_auf_user(userid) == False:
        data = (userid,user_name,0,0)
        await sqlite_db_users.sql_add_user(data)

    await bot.send_message(userid, get_text('on_startup'),reply_markup=start_markup())

# ловим нажатия на к=текстовые кнопки прифиля\инструкций\контактов\назад\получене токена
async def profile_message(message: types.Message):
    userid = message.from_user.id
    await bot.send_message(userid, get_profile(userid),reply_markup=profile_markup())

async def instruction_message(message: types.Message):
    userid = message.from_user.id
    await bot.send_message(userid, get_text('instruction'),reply_markup=start_markup())

async def contsacts_message(message: types.Message):
    userid = message.from_user.id
    await bot.send_message(userid, get_text('contacts'),reply_markup=start_markup())

async def back_message(message: types.Message):
    userid = message.from_user.id
    await bot.send_message(userid, 'Главное меню', reply_markup=start_markup())

async def get_token_message(message: types.Message):
    userid = message.from_user.id
    await bot.send_message(userid, 'Выберите сервис',reply_markup=services_markup())


# ловим сервис который выбрал пользователь
async def service1_message(message: types.Message):
    userid = message.from_user.id
    balance = get_balance(userid)
    if int(balance) >= int(get_text('price_first')): # проверяем баланс если все хорошо то списывваем денбги с баланса и выдаем токен
        await bot.send_message(userid, 'Обрабатываю ваш запрос',reply_markup=types.ReplyKeyboardRemove())
        # token_to_user = func()   вызвать функцию получения токена
        # await sqlite_db_users.sql_decrease_balance(get_text('price_first'),userid) функция уменьшения баланса разкоменитровать после подключения скрипта выше
        today = datetime.now().strftime('%d.%m.%Y')
        data = (SERVICE_FIRST,today,userid)
        await sqlite_db_users.sql_add_transaction(data) #внесение в базу данных
    else:
        await bot.send_message(userid, 'недостаточно средств',reply_markup=start_markup())

async def service2_message(message: types.Message):
    userid = message.from_user.id
    balance = get_balance(userid)
    if int(balance) >= int(get_text('price_second')):
        await bot.send_message(userid, 'Обрабатываю ваш запрос',reply_markup=types.ReplyKeyboardRemove())
        # token_to_user = func()   вызвать функцию получения токена
        # await sqlite_db_users.sql_decrease_balance(get_text('price_first'),userid) функция уменьшения баланса разкоменитровать после подключения скрипта выше
        today = datetime.now().strftime('%d.%m.%Y')
        data = (SERVICE_SECOND,today,userid)
        await sqlite_db_users.sql_add_transaction(data) #внесение в базу данных
    else:
        await bot.send_message(userid, 'недостаточно средств',reply_markup=start_markup())

async def service3_message(message: types.Message):
    userid = message.from_user.id
    balance = get_balance(userid)
    if int(balance) >= int(get_text('price_third')):
        await bot.send_message(userid, 'Обрабатываю ваш запрос',reply_markup=types.ReplyKeyboardRemove())
        # token_to_user = func()   вызвать функцию получения токена
        # await sqlite_db_users.sql_decrease_balance(get_text('price_first'),userid) функция уменьшения баланса разкоменитровать после подключения скрипта выше
        today = datetime.now().strftime('%d.%m.%Y')
        data = (SERVICE_THIRD,today,userid)
        await sqlite_db_users.sql_add_transaction(data) #внесение в базу данных
    else:
        await bot.send_message(userid, 'недостаточно средств',reply_markup=start_markup())


# ловим текстовую кнопку пополнения баланса
async def donate_message(message: types.Message):
    userid = message.from_user.id
    await bot.send_message(userid, 'Введите сумму пополнения',reply_markup=cancel_markup())
    await donateState.get_sum.set() # включаем состояние для получения суммы


# ловим с помощью машины состояний сумму пополнения
async def get_sum_message(message: types.Message, state=donateState.get_sum):
    userid = message.from_user.id
    if message.text != 'Отмена':
        async with state.proxy() as data:
            data['get_sum'] = message.text
        await bot.send_message(userid,'Отправьте чек')
        await donateState.get_chek.set()
    else:
        await bot.send_message(userid,'вы отменили транзакцию',reply_markup=start_markup())
        await state.finish()
    

# ловим чек 
async def get_chek_message(message: types.Message, state=donateState.get_chek):
    userid = message.from_user.id
    if message.text != 'Отмена':
        async with state.proxy() as data:
            data['get_chek'] = message.text
        # вызвать тут функцию проверки транзваакции  data['get_sum'] - сумма поплнения, data['get_chek'] - чек пользователя
        # ксли все хороо с транзакцие то запускать функцию изменения баланса | await sqlite_db_users.sql_increase_balance(data['get_sum'],userid)
        today = datetime.now().strftime('%d.%m.%Y')
        data = (userid,today,data['get_sum'])
        await sqlite_db_users.sql_add_donate(data) # внесение пополненния в базу данных
        await state.finish()
    else:
        await bot.send_message(userid,'вы отменили транзакцию',reply_markup=start_markup())
        await state.finish()


    
# регистрация всех хендлеров
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command,commands=['start'])

    dp.register_message_handler(profile_message,text=['Профиль'])
    dp.register_message_handler(get_token_message,text=['Получить токен'])
    dp.register_message_handler(donate_message,text=['Пополнить баланс'])

    dp.register_message_handler(service1_message,text=[SERVICE_FIRST])
    dp.register_message_handler(service2_message,text=[SERVICE_SECOND])
    dp.register_message_handler(service3_message,text=[SERVICE_THIRD])

    dp.register_message_handler(contsacts_message,text=['Контакты'])
    dp.register_message_handler(instruction_message,text=['Инструкции'])
    dp.register_message_handler(back_message,text=['👈 Назад'])

    dp.register_message_handler(get_sum_message,state=donateState.get_sum)
    dp.register_message_handler(get_chek_message, state=donateState.get_chek)

