#handlers/text_handlers.py

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from tg_bot_project.keyboards.inline_kb import educ_material_kb, schedule_kb
from tg_bot_project.utils.db import profile
from tg_bot_project.utils.request import ai_request

router = Router()

class SubState(StatesGroup):
    help_tg_id = State()
    ai_tg_id = State()

@router.message(F.text.lower() == "профиль" )
async def send_profile(message: types.Message):
    await message.answer(await profile(str(message.from_user.id)))

@router.message(F.text.lower() == "учебные материалы" )
async def send_ed(message: types.Message):
    await message.answer("Сслыка на облако с учебными материалами",
                         reply_markup=educ_material_kb())

@router.message(F.text.lower() == "помощь" )
async def start_help(message: types.Message, state: FSMContext):
    await message.answer("Напишите свой вопрос работнику поддержки")
    await state.set_state(SubState.help_tg_id)

@router.message(SubState.help_tg_id)
async def send_mes_to_admin(message: types.Message, state: FSMContext):
    await message.answer("Сообщение успешно отправлено!✅\nЖдите ответа от поддержки!")
    await message.bot.send_message(chat_id=8019661877,
                           text=f'TG ID пользователя:\n<code>{message.from_user.id}</code>\n\n'
                                f'Сообщение:\n{message.text}')
    await state.clear()

@router.message(F.text.lower() == "расписание" )
async def send_schedule(message: types.Message):
    await message.answer("📅 Показать расписание на:",
                         reply_markup=schedule_kb())

@router.message(F.text.lower() == "вопрос к ии" )
async def start_ai(message: types.Message, state: FSMContext):
    await message.answer("Напишите свой вопрос к ИИ")
    await state.set_state(SubState.ai_tg_id)


@router.message(SubState.ai_tg_id)
async def ans_ai(message: types.Message, state: FSMContext):
    await message.answer("Запрос отправлен!✅")
    await message.answer(await ai_request(str(message.text)))
    await state.clear()








