from aiogram.types import ReplyKeyboardMarkup
from misc.func_get_text import get_text

back_message = '👈 Назад'

# стартовый набор текстовых кнопок при [/start]
def start_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('Профиль')
    markup.add('Получить токен','Пополнить баланс')
    markup.add('Контакты','Инструкции')

    return markup

# выбор сервиса - три текстовые кнопки с выбором сервиса
def services_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(get_text('service_first'),get_text('service_second'),get_text('service_third'))

    return markup

# кнопки получить токен и пополнить баланс после входа в профиль
def profile_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('Получить токен','Пополнить баланс')
    markup.add(back_message)

    return markup

def cancel_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('Отмена')

    return markup

