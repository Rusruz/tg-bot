from aiogram import Router, F
from aiogram.types import Message
import pandas as pd

from nltk_module.nltk_main import get_response

router = Router(name=__name__)

last_answer = {"answer": "1"}


def answer_filter(message: Message):
    """Функция - фильтр, проверяет событие с обработкой вопроса бота(Хотите получить контакты отдела?(да/нет))"""

    return message.text.lower() == "да" and last_answer["answer"] == "Хотите получить контакты отдела?(да/нет)"


def answer_filter_no(message: Message):
    """Функция - фильтр, проверяет событие с обработкой вопроса бота(Хотите получить контакты отдела?(да/нет))"""

    return message.text.lower() == "нет" and last_answer["answer"] == "Хотите получить контакты отдела?(да/нет)"


@router.message(answer_filter)
async def handle_awaiting_contacts(message: Message):
    """Обработчик сообщения, если пользователь хочет получить контакты."""

    await message.answer("Иван Иванов ivan@example.com\n"
                         "Vasya Vasin vasya@vasin.ru\n"
                         "Елена Петрова petrova@mail.com\n"
                         "Борис Бритва boris@example.ru")


@router.message(answer_filter_no)
async def handle_no_answer(message: Message):
    """Обработчик сообщения, если пользователь не хочет получить контакты."""

    await message.answer("На нет и суда нет.")


@router.message(lambda message: len(message.text) == 6 and message.text.isdigit())
async def handle_art_info(message: Message):
    """Обработчик сообщения с 6-ти значным артикульным номером.
    Выдает информацию об артикуле из exсel файла."""

    df = pd.read_excel(r'C:\Users\Ruruz\PycharmProjects\tg-bot\ITEM_FE.xlsx')
    item_code = int(message.text)
    item_info = df[df['U_MGB'] == item_code][['U_MGB', 'Descr', 'U_ORIG_SUPP_DESC']]
    if not item_info.empty:

        row = item_info.iloc[0]
        response = (
            f"Артикул: {row['U_MGB']}\n"
            f"название: {row['Descr']}\n"
            f"Поставщик: {row['U_ORIG_SUPP_DESC']}"
        )

        await message.answer(response)
        #await message.answer("\n".join([str(value) for value in item_info.values[0]]))
    else:
        await message.answer("Артикул не найден.")


@router.message()
async def handle_user_message(message: Message):
    """Обработчик сообщений от пользователей.
    Распознает ключевые слова и на основе этого строит ответ."""

    response = get_response(message.text)
    last_answer["answer"] = response
    await message.answer(response)
