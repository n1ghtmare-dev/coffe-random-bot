from aiogram import Bot, Dispatcher
from config import settings
from handlers.common.start import router as start_router 


dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN.get_secret_value())

dp.include_router(start_router)
