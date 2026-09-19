# AIOGRAM

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# config
import config as cfg


#handlers
from handlers import start


bot = Bot(
    token=cfg.TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()



# ROUTERS
dp.include_router(start.router)


async def main():
    await dp.start_polling(bot)