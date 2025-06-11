import aiosqlite
import os
import asyncio

from .utils_func import format_student_info

DB_PATH = r"C:\Users\Public\PyProject\StudyBot\tg_bot_project\database.db"


async def login(username: str,
                     password: str,
                     tg_id: str,
                     tg_username: str
                     ) -> bool:
    try:
        # Проверяем существование файла
        if not os.path.exists(DB_PATH):
            raise FileNotFoundError(f"Database file not found at {DB_PATH}")

        async with aiosqlite.connect(DB_PATH) as db:

            await db.execute("PRAGMA foreign_keys = ON")

            cursor = await db.execute(
                "SELECT * FROM students WHERE login = ? AND password = ?",
                (username, password)
            )
            user = await cursor.fetchone()

            if bool(user) == True:
                await db.execute(
                    "UPDATE students  "
                    "SET tg_username = ?, tg_id = ?, is_authorized=1 "
                    "WHERE login = ?;",
                    (tg_username, tg_id, username, )
                )
                await db.commit()

            return bool(user)

    except aiosqlite.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

async def logout(tg_id: str
                        ) -> bool:
    try:
        if not os.path.exists(DB_PATH):
            raise FileNotFoundError(f"Database file not found at {DB_PATH}")

        async with aiosqlite.connect(DB_PATH) as db:

            await db.execute("PRAGMA foreign_keys = ON")

            cursor = await db.execute(
                "SELECT * FROM students WHERE tg_id = ? AND is_authorized=True",
                (tg_id, )
            )
            user = await cursor.fetchone()

            if bool(user) == True:
                await db.execute(
                    "UPDATE students  "
                    "SET is_authorized=False "
                    "WHERE tg_id = ?;",
                    (tg_id, )
                )
                await db.commit()

            return bool(user)

    except aiosqlite.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

async def profile(tg_id: str
                        ) -> str:
    try:
        if not os.path.exists(DB_PATH):
            raise FileNotFoundError(f"Database file not found at {DB_PATH}")

        async with aiosqlite.connect(DB_PATH) as db:

            await db.execute("PRAGMA foreign_keys = ON")

            cursor = await db.execute(
                "SELECT * FROM students WHERE tg_id = ? "
                "AND is_authorized=True;",
                (tg_id, )
            )
            rows = await cursor.fetchall()


            if rows:

                sub_list = [rows[0][1],
                            rows[0][2],
                            rows[0][3],
                            rows[0][4],
                            rows[0][5]]

                return format_student_info(sub_list)
            else:
                return "Вы не авторизованы"

    except aiosqlite.Error as e:
        return f"Database error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

