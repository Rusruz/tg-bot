from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router(name=__name__)

commands = ["/start", "/contacts", "/artinfo", "/help"]


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """Обработчик комманды /start"""

    await message.answer(f"Привет! Я бот для распознавания ключевых слов."
                         f"Задайте мне вопрос или напишите /help, чтобы узнать, что я умею.")


@router.message(Command("help"))
async def handle_help_command(message: Message):
    """Обработчик комманды /help"""

    await message.answer("Доступные комманды ⬇️\n"
                         "/start - приветствие\n"
                         "/about - информация о боте\n"
                         "/contacts - контакты отдела\n"
                         "/artinfo - информация об артикуле")


@router.message(Command("about"))
async def handle_about_command(message: Message):
    """Обработчик комманды /help"""

    await message.answer("Я простой бот, который реагирует на ключевые слова. Создан для демонстрации возможностей!")
