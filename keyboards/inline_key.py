from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# инлайн кнопки для садмин панели с редактированием контекста сообщений
inline_btn_on_startup = InlineKeyboardButton('Приветсвеный текст', callback_data='on_startup')
inline_btn_instruction = InlineKeyboardButton('инструкции', callback_data='instruction')
inline_btn_contacts = InlineKeyboardButton('контакты', callback_data='contacts')
inline_btn_price1 = InlineKeyboardButton('Цена 1', callback_data='price1')
inline_btn_price2 = InlineKeyboardButton('Цена 2', callback_data='price2')
inline_btn_price3 = InlineKeyboardButton('Цена 3', callback_data='price3')
inline_kb_change_text = InlineKeyboardMarkup(row_width=2)
inline_kb_change_text.add(inline_btn_on_startup,inline_btn_instruction,inline_btn_contacts,inline_btn_price1,inline_btn_price2,inline_btn_price3)


