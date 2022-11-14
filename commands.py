# Здесь что-то типа контроллера связывающий хендлеры и вью

from random import randint, random
from aiogram import types
from bot import bot

import model


# async def start(message: types.Message):
#     await view.greetings(message)

async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'до свидания!')
 
async def start(message: types.Message): 
    # model.setCount(int(model.getUserCount()))
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}\n'
                                                f'Это игра про конфеты! Смысл игры:\n'
                                                f'Вы с ботом по очереди берете конфеты. От 1 до 28 за раз. Кто берет последним, тот и выиграл')
    model.setFirstTurn()
    first_turn = model.getFirstTurn()
    if first_turn:
        await playerTake(message)
    else:
        await enemyTurn(message)

async def set_count(message: types.Message):
    count = message.text.split()
    if len(count) == 2:
        model.setUserCount(int(count[1]))
    await bot.send_message(message.from_user.id, f'Стартовое количество конфет изменено, '
                                                    f'на {model.getUserCount()}')

async def playerTake(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name},' 
                           f' берите конфеты (не более 28) ')

async def playerTurn(message: types.Message):
    take = None
    if message.text.isdigit(): 
        if int(message.text) < 0 or int(message.text) > 28:  
            await bot.send_message(message.from_user.id, f'Брать стоит не более 28 конфет')
        else: 
            take = int(message.text)
            model.setTake(take)
            model.setCount(model.getCount() - take)
            await bot.send_message(message.from_user.id, f'{message.from_user.username}, '
                                                        f'взял {model.getTake()} конфет, на столе осталось'
                                                        f' {model.getCount()}')
            if model.checkWin(): 
                await bot.send_message(message.from_user.id, f'Ты победил!' f' Начать игру заново - /newGame')
                return
            await enemyTurn(message)
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.username}, '
                                                    f'введите число')
    
async def enemyTurn(message: types.Message): 
    count = model.getCount()
    take = count%29 if count%29 != 0 else randint(1,28)
    model.setTake(take)
    model.setCount(count - take)
    await bot.send_message(message.from_user.id, f'Бот взял {model.getTake()} конфет, '
                                                f'на столе осталось {model.getCount()}')
    if model.checkWin(): 
        await bot.send_message(message.from_user.id, f'Бот победил!' f' Начать игру заново - /newGame')
        return
    await playerTake(message)
    
# async def newGame(message: types.Message):
# Пока мне не понятно, как восстановить количество конфет до нужного, что бы играть еще раз. 
# Может додумаюсь позжеюНо, срок сдачи ДЗ поджимает. 
# И мой вопрос про "Не понимаю что делать с ботом" подразумевал не создание bot.py и main.py, с этим то все как раз понятно. 
# Не понятно, а точнее, в моей голове пока не уложилась тема разделения на модули(отдельные файлы логику, отображение и т.п.)
