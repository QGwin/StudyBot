def format_student_info(student_data: list) -> str:

    if len(student_data) != 5:
        return "Ошибка: неверный формат входных данных"

    group, last_name, first_name, patronymic, student_id = student_data

    html_text = (
        f"<b>📌 Данные студента:</b>\n\n"
        f"<b>🎓 Группа:</b> <code>{group}</code>\n"
        f"<b>🆔 Номер зачётки:</b> <code>{student_id}</code>\n"
        f"<b>👤 ФИО:</b> {last_name} {first_name} {patronymic}\n\n"    
        f"<i>Для изменения данных обратитесь в деканат</i>"
    )

    return html_text

