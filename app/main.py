#!env python3

import asyncio
import os

from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()


dp = Dispatcher()


async def create_app():
    pass


@dp.message(CommandStart())
async def send_welcome(message: Message) -> None:
    await message.answer(f"Hello! I'm your friendly bot. {html.bold('Welcome!')}")


async def main() -> None:
    token = os.getenv("TELEGRAM_API_KEY")

    if type(token) is not str:
        print("Error: TELEGRAM_API_KEY environment variable is not set.")
        token = "7818556085:AAF-l7Vs0fdPiV4RLpETFqg81cvHfqgaJ3M"

    bot = Bot(token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
