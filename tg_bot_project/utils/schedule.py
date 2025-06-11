import pandas as pd
from datetime import datetime, timedelta


def get_schedule(day):
    try:
        # Читаем Excel-файл
        df = pd.read_excel(r'C:\Users\Public\PyProject\StudyBot\tg_bot_project\schedule.xlsx')

        # Словарь для преобразования номеров дней недели в русские названия
        weekdays_ru = {
            0: 'Понедельник',
            1: 'Вторник',
            2: 'Среда',
            3: 'Четверг',
            4: 'Пятница',
            5: 'Суббота',
            6: 'Воскресенье'
        }
        if day == "today":
            weekday_num = datetime.now().weekday()
            day_str="сегодня"
        elif day == "tomorrow":
            tomorrow = datetime.now() + timedelta(days=1)
            weekday_num = tomorrow.weekday()
            day_str = "завтра"

        today_weekday = weekdays_ru[weekday_num]

        # Фильтруем записи по дню недели
        day_schedule = df[df['День недели'] == today_weekday]

        if day_schedule.empty:
            return f"📅 На {day_str} ({today_weekday}) занятий нет"

        # Сортируем по времени
        day_schedule = day_schedule.sort_values('Время')

        # Форматируем результат
        formatted = f"📅 Расписание на {day_str} ({today_weekday}):\n\n"

        for _, row in day_schedule.iterrows():
            formatted += (
                f"🕒 {row['Время']} - {row['Предмет']}\n"
                f"🚪 Ауд. {row['Аудитория']} | 👨‍🏫 {row['Преподаватель']}\n"
                f"————————————————\n"
            )

        return formatted

    except FileNotFoundError:
        return "❌ Файл расписания не найден"
    except Exception as e:
        return f"❌ Ошибка: {str(e)}"


