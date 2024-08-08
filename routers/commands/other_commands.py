from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router(name=__name__)


@router.message(Command("contacts"))
async def handle_contacts_command(message: Message):
    """Обработчик команды /contacts.
    На запрос пользователя отправляет контакты."""

    await message.answer("Иван Иванов ivan@example.com\n"
                         "Vasya Vasin vasya@vasin.ru\n"
                         "Елена Петрова petrova@mail.com\n"
                         "Борис Бритва boris@example.ru")


@router.message(Command("artinfo"))
async def handle_contacts_command(message: Message):
    """Обработчик команды /artinfo."""

    await message.answer("Введите 6-ти значный код.\n"
                         "Например:\n"
                         "206460\n"
                         "208124\n"
                         "208713\n"
                         "307143\n"
                         "517814")
