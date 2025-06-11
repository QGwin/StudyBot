from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
import logging
from aiogram.types import CallbackQuery

from keyboard import *
from sql_connect import *
from func import *

from dotenv import load_dotenv
import os
load_dotenv()

Token_API = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(Token_API)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    try:
        if message.from_user.id != os.getenv("admin"):
            await message.answer(com_start(),
                                        parse_mode='HTML',
                                        reply_markup=main_kb())

        elif message.from_user.id == os.getenv("admin"):
            await message.answer(mes_for_admin(),
                                        parse_mode='HTML',
                                        reply_markup=main_kb())

        await message.delete()
    except Exception as ex:
        print(ex)

@dp.message(Command('help'))
async def cmd_start(message: types.Message):
    try:
        await message.answer(com_help(),
                                        parse_mode='HTML')
        await message.delete()
    except Exception as ex:
        print(ex)

@dp.message()
async def hot_mes(message):
    try:
        if message.text.lower() == 'учебные материалы':
            await message.answer(mes_study_file(),
                                        parse_mode='HTML')

        elif message.text.lower() == 'расписание?':
            await message.answer(mes_schedule(),
                                        parse_mode='HTML')

        elif message.text.lower() == 'локаия':
            await message.answer(mes_ai(),
                                        parse_mode='HTML')

        elif message.text.lower() == 'помощь':
            await message.answer(mes_helping(),
                                        parse_mode='HTML')

        elif message.text.lower() == 'профиль':
            await message.answer(mes_profile(),
                                        parse_mode='HTML')

    except Exception as ex:
        await message.answer(ex,
                             parse_mode='HTML')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        pass

