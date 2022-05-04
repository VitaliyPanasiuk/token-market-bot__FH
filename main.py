from config import dp
from aiogram import executor

from data_base import postgre_db
from handlers import client, admin


# выполнение при сфункций при старте
async def on_startup(dp):
    print('bot online')
    postgre_db.sql_start_products()  # подключение к бд


# регистрация хендлеров
admin.register_handlers_admin(dp)
client.register_handlers_client(dp)


executor.start_polling(dp, on_startup=on_startup,  skip_updates=True)
