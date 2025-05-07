import asyncio
from core.dispatcher import dp, bot
from database.core import db_manager
from database.models.base import Base


async def main() -> None:
    await db_manager.create_tables(Base)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

