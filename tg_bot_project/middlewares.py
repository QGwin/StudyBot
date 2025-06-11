from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, Update
from typing import Callable, Awaitable, Any
import aiosqlite


class AuthMiddleware(BaseMiddleware):
    def __init__(self, db_path: str):
        self.DB_PATH = db_path
        self.excluded_routers = excluded_routers or []
        super().__init__()

    async def __call__(
            self,
            handler: Callable[[Update, dict], Awaitable[Any]],
            event: Update,
            data: dict
    ) -> Any:


        # Получаем объект пользователя в зависимости от типа апдейта
        if event.message:
            user_id = event.message.from_user.id
            message_text = event.message.text
        elif event.callback_query:
            user_id = event.callback_query.from_user.id
            message_text = None
        else:
            return await handler(event, data)

        # Пропускаем команды авторизации
        if message_text and any(
                cmd in message_text.lower()
                for cmd in ['/start', '/login', '/register']
        ):
            return await handler(event, data)

        try:
            async with aiosqlite.connect(self.DB_PATH) as db:
                cursor = await db.execute(
                    "SELECT is_authorized FROM students WHERE tg_id = ?",
                    (str(user_id),))
                result = await cursor.fetchone()

                if result and result[0]:  # Если авторизован
                    return await handler(event, data)

        except aiosqlite.Error as e:
            print(f"Database error: {e}")
            await self._send_access_denied(event)
            return

        await self._send_access_denied(event)
        return

    async def _send_access_denied(self, event: Update):
        message = "🔒 Доступ запрещен. Пожалуйста, авторизуйтесь через /login"

        if event.message:
            await event.message.answer(message)
        elif event.callback_query:
            await event.callback_query.message.edit_text(message)