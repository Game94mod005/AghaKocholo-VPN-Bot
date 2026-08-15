import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message()
async def start(message: Message):
    await message.answer("🔥 AghaKocholo VPN Bot فعال شد ✅")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
