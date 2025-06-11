from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_kb():
    kb_list = [
        [KeyboardButton(text="Учебные материалы")],
        [KeyboardButton(text="Расписание"), KeyboardButton(text="Вопрос к ИИ")],
        [KeyboardButton(text="Профиль"), KeyboardButton(text="Помощь")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    #one_time_keyboard=True - сворачивает клаву после кнопки
    return keyboard

def admin_kb():
    kb_list = [
        [KeyboardButton(text="Учебные материалы")],
        [KeyboardButton(text="Расписание"), KeyboardButton(text="Вопрос к ИИ")],
        [KeyboardButton(text="Профиль"), KeyboardButton(text="Помощь")],
        [KeyboardButton(text="Настройки")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return keyboard



def inline_kb(kb_list):

    kb_list = [
        [KeyboardButton(text="О нас")],
        [KeyboardButton(text="Где мы?"), KeyboardButton(text="Наши контакты")],
        [KeyboardButton(text="Тренерский состав"), KeyboardButton(text="Связь с администратором")],
    ]

    builder = InlineKeyboardBuilder()
    for i in kb_list:
        builder.row(
            InlineKeyboardButton(
                text=f'{i}',
                callback_data=i))
    builder.adjust(1)
    return builder.as_markup()

def url_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
                text="Сайт",
                url="https://www.psuti.ru/"))
    builder.adjust(1)
    return builder.as_markup()