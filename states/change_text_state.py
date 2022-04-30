from aiogram.dispatcher.filters.state import StatesGroup, State


#ОПИСЫВАЕТСЯ МАШИНА СОСТОЯНИЯ ДЛЯ ИЗИЕНИЯ ПЕРЕМЕННЫХ ТЕКСТОВ 
class changetext(StatesGroup):
    name = State()
    get_description = State()