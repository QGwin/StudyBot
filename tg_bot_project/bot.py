import asyncio
import logging
import colorlog

from handlers import (commands_router,
                      auth_router,
                      text_router,
                      admin_router,
                      callback_router)
from decouple import config

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

ADMIN_ID = config('ADMIN_ID')
BOT_TOKEN = config("BOT_TOKEN")

formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'bold_cyan',
        'INFO': 'bold_green',
        'WARNING': 'bold_yellow',
        'ERROR': 'bold_red',
        'CRITICAL': 'bold_purple',
    }
)

handler_color = logging.StreamHandler()
handler_color.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(handler_color)

if root_logger.handlers:
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
root_logger.addHandler(handler_color)

async def main():

    bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(
                  parse_mode=ParseMode.HTML))
    storage=MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_routers(
        commands_router,
                auth_router,
                text_router,
                admin_router,
                callback_router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except: pass