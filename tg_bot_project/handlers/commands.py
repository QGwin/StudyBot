#handlers/commands.py

from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from tg_bot_project.keyboards.kb import start_kb
router = Router()

@router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать!\n"
        "Для авторизации используйте команду:"
        "/login",
        reply_markup=start_kb()
    )

@router.message(Command("help"))
async def help_cmd(message: types.Message):
    help_text = """
<b>📚 Список доступных команд:</b>

<b>🔹 Основные команды:</b>
/start - Начать работу с ботом
/help - Показать это справочное сообщение

<b>🔹 Учетная запись:</b>
/login - Авторизоваться в системе
/logout - Выйти из системы

Для навигации используйте кнопки меню или вводите команды вручную.
    """
    await message.answer(help_text)