# Здесь хранятся хендлеры

from aiogram import Dispatcher

import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.finish, commands=['finish'])
    dp.register_message_handler(commands.set_count, commands=['set_count'])
    dp.register_message_handler(commands.set_count, commands=['newGame'])
    # dp.register_message_handler(commands.getNumber)
    dp.register_message_handler(commands.playerTurn)