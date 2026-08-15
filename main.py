import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InputMediaPhoto
)

from config import (
    BOT_TOKEN,
    ADMIN_ID,
    CARD_NUMBER,
    CARD_OWNER
)

from database import init_db

from keyboards import (
    main_menu,
    locations,
    volumes
)

from admin import (
    open_admin,
    admin_button
)

from shop import (
    set_location,
    set_plan,
    get_price,
    user_orders
)


bot = Bot(BOT_TOKEN)

dp = Dispatcher()


# ذخیره وضعیت کاربران
waiting_receipt = {}



# 🏠 شروع

@dp.message(F.text == "/start")
async def start(message: Message):

    await message.answer(

        "🔥💎 AghaKocholo VPN 💎🔥\n\n"

        f"سلام {message.from_user.first_name} 👋\n\n"

        "🚀 سرویس‌های پرسرعت VPN\n"
        "🌍 لوکیشن‌های مختلف\n"
        "⚡ فعال‌سازی سریع\n\n"

        "یکی از گزینه‌ها را انتخاب کنید 👇",

        reply_markup=main_menu()

    )



# 👑 ادمین

@dp.message(F.text == "/admin")
async def admin(message: Message):

    await open_admin(message)



# 💎 انتخاب Diamond

@dp.callback_query(F.data == "diamond")
async def diamond(callback: CallbackQuery):

    user_orders[callback.from_user.id] = {
        "type":"diamond"
    }

    await callback.message.answer(

        "💎 پلن الماس انتخاب شد\n\n"
        "🌍 کشور مورد نظر را انتخاب کنید:",

        reply_markup=locations()

    )

    await callback.answer()



# 👑 انتخاب Gold

@dp.callback_query(F.data == "gold")
async def gold(callback: CallbackQuery):

    user_orders[callback.from_user.id] = {
        "type":"gold"
    }

    await callback.message.answer(

        "👑 پلن طلایی انتخاب شد\n\n"
        "🌍 کشور را انتخاب کنید:",

        reply_markup=locations()

    )

    await callback.answer()



# 🌍 کشور

@dp.callback_query(F.data.startswith("loc_"))
async def location(callback: CallbackQuery):

    loc = callback.data.replace(
        "loc_",
        ""
    )

    set_location(
        callback.from_user.id,
        loc
    )


    await callback.message.answer(

        "📦 حجم سرویس را انتخاب کنید:",

        reply_markup=volumes()

    )


    await callback.answer()



# 📦 حجم

@dp.callback_query(F.data.startswith("vol_"))
async def volume(callback: CallbackQuery):

    vol = callback.data.replace(
        "vol_",
        ""
    )

    set_plan(
        callback.from_user.id,
        vol+"GB"
    )


    price = get_price(
        callback.from_user.id
    )


    waiting_receipt[
        callback.from_user.id
    ] = True


    await callback.message.answer(

        "✅ سفارش شما ثبت شد\n\n"

        f"📦 حجم: {vol}GB\n"
        f"💰 مبلغ: {price:,} تومان\n\n"

        "💳 اطلاعات پرداخت:\n"

        f"{CARD_NUMBER}\n"

        f"👤 {CARD_OWNER}\n\n"

        "بعد از پرداخت، عکس رسید را ارسال کنید 📸🔥"

    )


    await callback.answer()



# 📸 دریافت رسید

@dp.message(F.photo)
async def receipt(message: Message):

    user_id = message.from_user.id


    if user_id not in waiting_receipt:

        return


    photo = message.photo[-1].file_id


    await bot.send_photo(

        ADMIN_ID,

        photo,

        caption=

        "🔔 سفارش جدید\n\n"

        f"👤 کاربر:\n"
        f"{message.from_user.full_name}\n\n"

        "📸 رسید پرداخت ارسال شد\n\n"

        "برای تایید بررسی کنید."

    )


    await message.answer(

        "✅ رسید شما ارسال شد\n\n"
        "⏳ منتظر تایید ادمین باشید."

    )


    del waiting_receipt[user_id]



# دکمه های ادمین

@dp.callback_query()
async def all_callbacks(callback: CallbackQuery):

    await admin_button(callback)



async def main():

    await init_db()

    print(
        "🔥 AghaKocholo VPN PRO Started"
    )

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
