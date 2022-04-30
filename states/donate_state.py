from aiogram.dispatcher.filters.state import StatesGroup, State


# ОПИСЫВАЕТЬСЯ МАШИНА СОСТОЯНИЯ ДЛЯ ПОПОЛНЕНИЯ БАЛАНСА
class donateState(StatesGroup):
    get_sum = State()
    get_chek = State()