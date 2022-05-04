
from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "5155022720:AAEBpPfi-SmyRXv4gR_kSbW_7kgQThLWcUs"
DB_URI = "postgres://qagcztswbjprcu:20185d1a69f0f714fc1746f22fab1b920a01c0faf2c4f7eb419874c77ba11581@ec2-34-227-120-79.compute-1.amazonaws.com:5432/d7ktqajpvkpl6m"

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# list of admins
admins = [762342298, 727336232]
