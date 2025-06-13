#keyboards/kb.py

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def main_kb():
    kb_list = [
        [KeyboardButton(text="Учебные материалы")],
        [KeyboardButton(text="Расписание"), KeyboardButton(text="Вопрос к ИИ")],
        [KeyboardButton(text="Профиль"), KeyboardButton(text="Помощь")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
                                   resize_keyboard=True)
    return keyboard

def start_kb():
    kb_list = [
        [KeyboardButton(text="/login")],
        ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
                                   resize_keyboard=True,
                                   one_time_keyboard=True)
    return keyboard