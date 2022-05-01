from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "5155022720:AAEBpPfi-SmyRXv4gR_kSbW_7kgQThLWcUs"

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# list of admins
admins = [762342298, 727336232]
