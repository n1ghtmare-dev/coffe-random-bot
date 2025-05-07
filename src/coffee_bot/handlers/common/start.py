from aiogram import Router, types 
from aiogram.filters import Command
from messages.common import CommonMessages 
from database.crud.users import create_user, get_user, user_exists
from schemas.users import UserCreate


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    user_exist = await user_exists(user_id)
    if not user_exist:
        user_data = UserCreate(
            first_name="",
            second_name="",
            last_name="",
            position="",
            group="",
            user_id=user_id,
        )
        user = await create_user(user_data)

    await message.answer(CommonMessages.START)


