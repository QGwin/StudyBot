from aiogram import Router, types, F
from tg_bot_project.utils.schedule import get_schedule

router = Router()

@router.callback_query(F.data.in_(["today", "tomorrow"]))
async def callback_today(callback: types.CallbackQuery):
    schedule = get_schedule(callback.data)
    await callback.message.edit_text(
        f"{schedule}")
    await callback.answer()