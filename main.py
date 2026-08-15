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
    reject_order,
    save_config
)


bot = Bot(BOT_TOKEN)

dp = Dispatcher()


# نگهداری سفارش آخر کاربر
user_last_order = {}


# =========================
# START
# =========================

@dp.message(F.text == "/start")
async def start(message: Message):

    await message.answer(
        "🔥💎 AghaKocholo VPN 💎🔥\n\n"
        f"سلام {message.from_user.first_name} 👋\n\n"
        "🚀 خرید VPN پرسرعت\n"
        "🌍 لوکیشن‌های مختلف\n"
        "⚡ فعال‌سازی سریع\n\n"
        "انتخاب کنید 👇",

        reply_markup=main_menu()
    )



# =========================
# ADMIN
# =========================

@dp.message(F.text == "/admin")
async def admin(message: Message):

    if message.from_user.id == ADMIN_ID:

        from admin import open_admin

        await open_admin(message)



# =========================
# PLAN
# =========================

@dp.callback_query(F.data == "diamond")
async def diamond(callback: CallbackQuery):

    user_orders[callback.from_user.id] = {
        "type":"diamond"
    }


    await callback.message.answer(
        "💎 پلن الماس انتخاب شد\n\n"
        "🌍 لوکیشن را انتخاب کنید:",
        reply_markup=locations()
    )

    await callback.answer()



@dp.callback_query(F.data == "gold")
async def gold(callback: CallbackQuery):

    user_orders[callback.from_user.id] = {
        "type":"gold"
    }


    await callback.message.answer(
        "👑 پلن طلایی انتخاب شد\n\n"
        "🌍 لوکیشن را انتخاب کنید:",
        reply_markup=locations()
    )

    await callback.answer()



# =========================
# LOCATION
# =========================

@dp.callback_query(F.data.startswith("loc_"))
async def loc(callback: CallbackQuery):

    location = callback.data.replace(
        "loc_",
        ""
    )


    set_location(
        callback.from_user.id,
        location
    )


    await callback.message.answer(
        "📦 حجم را انتخاب کنید:",
        reply_markup=volumes()
    )

    await callback.answer()



# =========================
# VOLUME + ORDER
# =========================

@dp.callback_query(F.data.startswith("vol_"))
async def volume(callback: CallbackQuery):

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


    user_last_order[
        callback.from_user.id
    ] = order_id



    await callback.message.answer(

        "✅ سفارش شما ساخته شد\n\n"

        f"📦 حجم: {volume}\n"
        f"💰 مبلغ: {price:,} تومان\n\n"

        "💳 پرداخت کنید:\n"

        f"{CARD_NUMBER}\n"
        f"👤 {CARD_OWNER}\n\n"

        "بعد از پرداخت عکس رسید را ارسال کنید 📸"

    )


    await callback.answer()



# =========================
# RECEIPT
# =========================

@dp.message(F.photo)
async def photo(message: Message):

    user_id = message.from_user.id


    if user_id not in user_last_order:
        return


    order_id = user_last_order[user_id]


    photo_id = message.photo[-1].file_id


    await add_receipt(
        order_id,
        photo_id
    )


    await bot.send_photo(

        ADMIN_ID,

        photo_id,

        caption=

        "🔔 سفارش جدید\n\n"

        f"👤 کاربر:\n"
        f"{message.from_user.full_name}\n\n"

        f"🆔 سفارش: #{order_id}\n\n"

        "بررسی کنید 👇",

        reply_markup=receipt_buttons(order_id)

    )


    await message.answer(
        "✅ رسید ارسال شد\n\n"
        "⏳ منتظر تایید باشید."
    )



# =========================
# ADMIN APPROVE / REJECT
# =========================

@dp.callback_query(F.data.startswith("approve_"))
async def approve(callback: CallbackQuery):

    if callback.from_user.id != ADMIN_ID:
        return


    order_id = int(
        callback.data.split("_")[1]
    )


    await approve_order(order_id)


    await callback.message.answer(
        "✅ پرداخت تایید شد\n\n"
        "حالا کانفیگ را ارسال کنید."
    )


    await callback.answer()



@dp.callback_query(F.data.startswith("reject_"))
async def reject(callback: CallbackQuery):

    if callback.from_user.id != ADMIN_ID:
        return


    order_id = int(
        callback.data.split("_")[1]
    )


    await reject_order(order_id)


    await callback.message.answer(
        "❌ پرداخت رد شد."
    )


    await callback.answer()



# =========================
# MAIN
# =========================

async def main():

    await init_db()

    print(
        "🔥 AghaKocholo VPN PRO ONLINE"
    )

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
