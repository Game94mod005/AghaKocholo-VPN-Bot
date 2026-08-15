import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import BOT_TOKEN, ADMIN_ID

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def messages(message: Message):

    if message.text == "/start":
        await message.answer(
            "🔥 AghaKocholo VPN\n\n"
            "خوش آمدید 👋\n\n"
            "🛒 خرید VPN\n"
            "📦 سرویس‌های من\n"
            "💳 کیف پول\n"
            "🆘 پشتیبانی"
        )

    elif message.text == "/admin":
        if message.from_user.id == ADMIN_ID:
            await message.answer(
                "👑 پنل مدیریت\n\n"
                "📊 آمار\n"
                "📦 سفارش‌ها\n"
                "👥 کاربران\n"
                "⚙ تنظیمات"
            )
        else:
            await message.answer("❌ دسترسی ندارید")


async def main():
    print("🔥 AghaKocholo VPN Bot Started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
