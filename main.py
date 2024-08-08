import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from routers import router as main_router


TOKEN = "7096229954:AAHumK4yC_Q1ZQVrbWNJT5V_PGXWiHIG2gs"


async def main() -> None:
    """Основная функция. При вызове запускает тг-бота."""

    dp = Dispatcher()
    dp.include_router(main_router)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
