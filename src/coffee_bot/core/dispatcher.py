from aiogram import Bot, Dispatcher
from config import settings
from handlers.common.start import router as start_router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties


dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp.include_router(start_router)

