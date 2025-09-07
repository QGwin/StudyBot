#handlers/auth.py

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from decouple import config
from message_text import message_for_start
from keyboard import user_kb

router = Router()

admin_id=882880478

class AdminState(StatesGroup):
    admin_username = State()
    admin_password = State()

class QueryState(StatesGroup):
    id = State()

@router.message(Command("start"))
async def start_auth_admin(message: types.Message):
    await message.answer(message_for_start(message.from_user.full_name),
                           reply_markup=user_kb())

@router.message(Command("admin"))
async def start_auth_admin(message: types.Message, state: FSMContext):
    await message.answer("Введите ваш логин:")
    await state.set_state(AdminState.admin_username)


@router.message(AdminState.admin_username)
async def process_login(message: types.Message, state: FSMContext):
    if message.text == config('ADMIN_LOGIN'):
        await state.update_data(login=message.text)
        await message.answer("Введите пароль:")
        await state.set_state(AdminState.admin_password)
    else:
        await message.answer("❌ Неверный логин")


@router.message(AdminState.admin_password)
async def process_password(message: types.Message, state: FSMContext):
    if message.text == config('ADMIN_PASSWORD'):
        await message.answer("✅ Авторизация прошла успешно")
        global admin_id
        admin_id=message.from_user.id

    else:
        await message.answer("❌ Неверный логин или пароль")

    await state.clear()

@router.message(F.text.lower() == "предложение")
async def start_bid(message: types.Message, state: FSMContext):
    await message.answer("Жду ваше сообщение для отправки")
    await state.set_state(QueryState.id)

@router.message(QueryState.id)
async def process_bid(message: types.Message, state: FSMContext):
    await message.answer("Сообщение успешно отправлено!✅")
    await message.bot.send_message(chat_id=admin_id,
                                   text=f'Сообщение от пользователя: @{message.from_user.username}\n\n'
                                        f'Сообщение:\n{message.text}')
    await state.clear()