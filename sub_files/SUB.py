from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.methods import DeleteWebhook
from aiogram.client.default import DefaultBotProperties
import asyncio
import logging
from func import *


logging.basicConfig(level=logging.INFO)

bot = Bot(token="7872237409:AAFP50sM9spRtvjvMpfuH5ZSXeDNdFl9CZE",
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command('help'))
async def cmd_start(message: types.Message):
    await message.answer(com_help())
    await message.delete()

@dp.message()
async def hot_mes(message):
    try:
        if message.text.lower() == 'сообщение':
            await message.answer("ответ")

        elif message.text.lower() == 'картинка':
            await bot.send_photo(chat_id=message.from_user.id,
                                     photo="https://shikimori.one/system/screenshots/original/ff441034a8aab8f6d430a3463e5986363db004f1.jpg?1673110517")

        elif message.text.lower() == 'локация':
            await bot.send_location(chat_id=message.from_user.id,
                                    latitude=53.201012,
                                    longitude=50.099186)

        elif message.text.lower() == 'стикер':
            await bot.send_sticker(chat_id=message.from_user.id,
                                   sticker="CAACAgIAAxkBAAMYaD-u72nxrsI-L7SdNPzpZUwXaiAAAt9vAAICuPhIbI0egWF5BzI2BA")

        elif message.sticker:
            await message.reply(message.sticker.file_id)

    except Exception as ex:
        if message.sticker:
            await message.reply(message.sticker.file_id)
        else:
            await message.answer(ex,
                             parse_mode='HTML')

# @dp.message()
# async def send_sticker_id(message: types.Message):
#     await message.answer(message.sticker.file_id)


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        pass

