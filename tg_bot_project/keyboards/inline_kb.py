from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def educ_material_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
                text="📕 Учебные материалы",
                url="https://disk.yandex.ru/d/vOmsU58y1bBF_w"))
    builder.adjust(1)
    return builder.as_markup()

def schedule_kb():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Сегодня", callback_data="today"),
        InlineKeyboardButton(text="Завтра", callback_data="tomorrow")
    )
    builder.adjust(2)
    return builder.as_markup()