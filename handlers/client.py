from aiogram import types, Dispatcher

from create_bot import bot
from data_base import sqlite_db
from keyboards import kb_client


async def command_start(message: types.Message):
    await message.answer('C заботой о Вашем питомце!', reply_markup=kb_client)


async def operating_mode_command(message: types.Message):
    await message.answer('Ежедневно с 09-21ч')


async def location_command(message: types.Message):
    await message.answer('г.Уфа, ул.Ю.Гагарина 41/3')


async def services_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(operating_mode_command, commands=['Режим_работы'])
    dp.register_message_handler(location_command, commands=['Расположение'])
    dp.register_message_handler(services_command, commands=['Услуги'])
