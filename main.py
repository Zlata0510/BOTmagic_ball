import asyncio
from email import message

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

import AI
from config import config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Привет! Я - Магический Шар. Задай вопрос, и ты получишь ответ на него.')


@dp.message(F.text)
async def write(message: Message):
    answer = AI.generate_answer()
    await message.answer(answer)


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')