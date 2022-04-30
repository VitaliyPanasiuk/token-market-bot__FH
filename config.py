from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "5257942822:AAFqBBqGZs6UJZsF3fJ6fY-f8pCFQelxXRw"

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# list of admins
admins = [762342298]
