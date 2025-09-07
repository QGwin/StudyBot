#keyboards/kb.py

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def user_kb():
    kb_list = [
        [KeyboardButton(text="Предложение")],
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