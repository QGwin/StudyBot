#handlers/auth.py

from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from tg_bot_project.utils.db import login, logout
from tg_bot_project.keyboards.kb import main_kb

router = Router()

class AuthState(StatesGroup):
    login_username = State()
    login_password = State()

@router.message(Command("login"))
async def start_login(message: types.Message, state: FSMContext):
    await message.answer("Введите ваш логин:")
    await state.set_state(AuthState.login_username)


@router.message(AuthState.login_username)
async def process_login_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer("Введите пароль:")
    await state.set_state(AuthState.login_password)

@router.message(AuthState.login_password)
async def process_login_password(message: types.Message, state: FSMContext):
    data = await state.get_data()
    username = data["username"]
    password = message.text
    user_data_id=str(message.from_user.id)
    user_data_username="@"+message.from_user.username
    if await login(username, password,user_data_id, user_data_username):

        await message.answer("✅ Авторизация прошла успешно",
                             reply_markup=main_kb())
    else:
        await message.answer("❌ Неверный логин или пароль")

    await state.clear()

@router.message(Command("logout"))
async def start_login(message: types.Message, state: FSMContext):
    if await logout(str(message.from_user.id)):
        await message.answer("Выполнен выход из профиля")
    else:
        await message.answer("Вы ещё не авторизированны")