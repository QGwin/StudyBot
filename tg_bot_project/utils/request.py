#utils/request.py

import requests

from decouple import config

API_KEY = config('AI_API')
URL_AI = config('URL_AI')

async def ai_request(message: str) -> str:
    sub_mes = " не используй никаких знаков кроме знаков препинания"
    request_json = {
        "message": message+sub_mes,
        "api_key": API_KEY
    }

    response = requests.post(url=URL_AI,
                             json=request_json)

    if response.status_code != 200:
        return f'Ошибка! Код http-ответа: {response.status_code}'
    else:
        resp_json = response.json()

        if resp_json['is_success']:
            resp_msg = resp_json['response']
            used_words = resp_json['used_words_count']
            print(f'Потрачено слов: {used_words}')
            return f'Ответ от бота: {resp_msg}'
        else:
            error = resp_json['error_message']
            return f'Ошибка: {error}'