#!env python3
import asyncio
from dotenv import load_dotenv
from internal import db, logger
from internal.config import Config
from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from plugins import start_handler
from aiogram.client.default import DefaultBotProperties

load_dotenv()

dp = Dispatcher()

# Registers all the function to handle incoming Telegram messages that use the command.
dp.message.register(start_handler, Command(commands=["start"]))

async def main() -> None:
    await db.init_db()
    config = Config()
    if not config.botApi:
        logger.error("Missing botApi environment variable")
        return
    bot = Bot(config.botApi, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())