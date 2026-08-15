import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery

from config import BOT_TOKEN, ADMIN_ID, CARD_NUMBER, CARD_OWNER
from keyboards import main_menu, admin_menu
from database import init_db


bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):

    await message.answer(
        f"🔥 AghaKocholo VPN\n\n"
        f"سلام {message.from_user.first_name} 👋\n\n"
        f"به ربات فروش VPN خوش آمدید.\n\n"
        f"یکی از گزینه‌ها را انتخاب کنید:",
        reply_markup=main_menu()
    )


@dp.message(F.text == "/admin")
async def admin(message: Message):

    if message.from_user.id == ADMIN_ID:

        await message.answer(
            "👑 پنل مدیریت AghaKocholo\n\n"
            "به پنل خوش آمدید.",
            reply_markup=admin_menu()
        )

    else:

        await message.answer(
            "❌ شما دسترسی ادمین ندارید."
        )


@dp.callback_query(F.data == "buy")
async def buy(callback: CallbackQuery):

    await callback.message.answer(
        "🛒 انتخاب پلن VPN\n\n"

        "🇩🇪 Germany Premium\n"
        "📦 20GB\n"
        "⏳ 30 روز\n"
        "💰 80,000 تومان\n\n"

        "برای خرید مبلغ را پرداخت کنید:\n\n"

        f"💳 کارت:\n{CARD_NUMBER}\n\n"
        f"👤 به نام:\n{CARD_OWNER}\n\n"

        "بعد از پرداخت، عکس رسید را ارسال کنید."
    )

    await callback.answer()


@dp.callback_query(F.data == "services")
async def services(callback: CallbackQuery):

    await callback.message.answer(
        "📦 شما هنوز سرویسی ندارید."
    )

    await callback.answer()


@dp.callback_query(F.data == "support")
async def support(callback: CallbackQuery):

    await callback.message.answer(
        "🆘 پشتیبانی:\n"
        "@YourUsername"
    )

    await callback.answer()



async def main():

    await init_db()

    print("🔥 AghaKocholo VPN Started")

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())    print("🔥 AghaKocholo VPN Bot Started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
