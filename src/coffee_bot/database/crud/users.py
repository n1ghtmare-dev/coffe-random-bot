from sqlalchemy import select
from database.models.users import User
from database.core import db_manager
from schemas.users import UserCreate 


# TODO: compose functions into a class 

async def create_user( 
    user_in: UserCreate,
):
    async with db_manager.session() as session:
        user = User(**user_in.model_dump())
        session.add(user)
        await session.commit()
        return user

async def get_user(
    user_id: int,
):
    async with db_manager.session() as session:
        return await session.get(User, user_id)

async def user_exists(
    user_id: int,
):
    user = await get_user(user_id)
    return user is not None

