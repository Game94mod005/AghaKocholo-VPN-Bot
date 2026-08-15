import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery

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
    volumes,
    receipt_buttons
)

from shop import (
    user_orders,
    set_location,
    set_plan,
    get_price
)

from orders import (
    create_order,
    add_receipt,
    approve_order,
    reject_order
)

from admin import (
    open_admin,
    approve_order as admin_approve,
    reject_order as admin_reject,
    receive_config
)


bot = Bot(BOT_TOKEN)

dp = Dispatcher()


# نگهداری سفارش‌های فعال
active_orders = {}


# =====================
# START
# =====================

@dp.message(F.text == "/start")
async def start(message: Message):

    await message.answer(
        "🔥💎 AghaKocholo VPN 💎🔥\n\n"

        f"سلام {message.from_user.first_name} 👋\n\n"

        "🚀 فروش سرویس VPN پرسرعت\n"
        "🌍 لوکیشن‌های مختلف\n"
        "⚡ فعال‌سازی سریع\n\n"

        "از منوی زیر انتخاب کن 👇",

        reply_markup=main_menu()
    )


# =====================
# ADMIN
# =====================

@dp.message(F.text == "/admin")
async def admin(message: Message):

    await open_admin(message)



# =====================
# خرید Diamond
# =====================

@dp.callback_query(F.data == "diamond")
async def diamond(callback: CallbackQuery):

    user_orders[callback.from_user.id] = {
        "type": "diamond"
    }

    await callback.message.answer(
        "💎 پلن الماس انتخاب شد\n\n"
        "🌍 کشور را انتخاب کن:",
        reply_markup=locations()
    )

    await callback.answer()



# =====================
# خرید Gold
# =====================

@dp.callback_query(F.data == "gold")
async def gold(callback: CallbackQuery):

    user_orders[callback.from_user.id] = {
        "type": "gold"
    }

    await callback.message.answer(
        "👑 پلن طلایی انتخاب شد\n\n"
        "🌍 کشور را انتخاب کن:",
        reply_markup=locations()
    )

    await callback.answer()



# =====================
# کشور
# =====================

@dp.callback_query(F.data.startswith("loc_"))
async def choose_location(callback: CallbackQuery):

    location = callback.data.replace(
        "loc_",
        ""
    )

    set_location(
        callback.from_user.id,
        location
    )

    await callback.message.answer(
        "📦 حجم سرویس را انتخاب کن:",
        reply_markup=volumes()
    )

    await callback.answer()



# =====================
# حجم و قیمت
# =====================

@dp.callback_query(F.data.startswith("vol_"))
async def choose_volume(callback: CallbackQuery):

    volume = callback.data.replace(
        "vol_",
        ""
    ) + "GB"


    set_plan(
        callback.from_user.id,
        volume
    )


    price = get_price(
        callback.from_user.id
    )


    order_id = await create_order(
        callback.from_user.id,
        volume,
        price
    )


    active_orders[
        callback.from_user.id
    ] = order_id



    await callback.message.answer(

        "✅ سفارش ساخته شد 🔥\n\n"

        f"📦 حجم: {volume}\n"
        f"💰 مبلغ: {price:,} تومان\n\n"

        "💳 اطلاعات پرداخت:\n"

        f"{CARD_NUMBER}\n"
        f"👤 {CARD_OWNER}\n\n"

        "بعد از پرداخت عکس رسید را بفرست 📸"

    )


    await callback.answer()



# =====================
# دریافت رسید
# =====================

@dp.message(F.photo)
async def receive_receipt(message: Message):

    user_id = message.from_user.id


    if user_id not in active_orders:
        return


    order_id = active_orders[user_id]


    photo_id = message.photo[-1].file_id


    await add_receipt(
        order_id,
        photo_id
    )


    await bot.send_photo(

        ADMIN_ID,

        photo_id,

        caption=

        "🔔 سفارش جدید 🔔\n\n"

        f"👤 کاربر:\n{message.from_user.full_name}\n\n"

        f"🆔 سفارش: #{order_id}\n\n"

        "بررسی پرداخت 👇",

        reply_markup=receipt_buttons(order_id)

    )


    await message.answer(
        "✅ رسید ارسال شد\n\n"
        "⏳ منتظر تایید باشید."
    )



# =====================
# تایید پرداخت
# =====================

@dp.callback_query(F.data.startswith("approve_"))
async def approve(callback: CallbackQuery):

    order_id = int(
        callback.data.split("_")[1]
    )


    await approve_order(order_id)


    await admin_approve(
        callback,
        order_id
    )


    await callback.answer()



# =====================
# رد پرداخت
# =====================

@dp.callback_query(F.data.startswith("reject_"))
async def reject(callback: CallbackQuery):

    order_id = int(
        callback.data.split("_")[1]
    )


    await reject_order(order_id)


    await admin_reject(
        callback,
        order_id
    )


    await callback.answer()



# =====================
# کانفیگ ادمین
# =====================

@dp.message(F.text.startswith("vless://"))
async def config(message: Message):

    await receive_config(message)



# =====================
# RUN
# =====================

async def main():

    await init_db()

    print(
        "🔥 AghaKocholo VPN PRO Running"
    )

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
