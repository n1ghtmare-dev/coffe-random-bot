from aiogram import Router, types 
from aiogram.filters import Command


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = """
    ☕ Добро пожаловать в CoffeeBot! 

    С нами ты можешь выбрать партнера для чашечки кофе!
    Команды:
    - Анкета
        Важно заполнить анкету, прежде чем искать партнера
    - Подбор
        Запусти поиск партнера
    """

    await message.answer(welcome_text)


