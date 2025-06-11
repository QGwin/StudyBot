from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

class IDState(StatesGroup):
    tg_id = State()
    mes = State()

@router.message(F.text.lower() == "ответ")
async def send_profile(message: types.Message, state: FSMContext):
    if message.from_user.id==8019661877:
        await message.answer("Напишите TG ID получателя")
        await state.set_state(IDState.tg_id)

@router.message(IDState.tg_id)
async def send_profile(message: types.Message, state: FSMContext):
    if message.from_user.id==8019661877:
        await state.update_data(tgid=message.text)
        await message.answer("Напишите сообщение")
        await state.set_state(IDState.mes)

@router.message(IDState.mes)
async def send_profile(message: types.Message, state: FSMContext):
    if message.from_user.id==8019661877:
        data = await state.get_data()
        tgid = data['tgid']
        await message.bot.send_message(chat_id=tgid,
                                       text=f'Сообщение от поддержки:\n\n{message.text}')
        await message.answer("Сообщение успешно пользователю!✅")
        await state.clear()