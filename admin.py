from aiogram.types import Message, CallbackQuery

from config import ADMIN_ID
from keyboards import admin_menu

# سفارش‌هایی که منتظر کانفیگ هستند
waiting_configs = {}


async def open_admin(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        "👑🔥 AghaKocholo VPN Admin Panel 🔥👑\n\n"
        "━━━━━━━━━━━━━━\n"
        "📊 آمار ربات\n"
        "🛒 مدیریت سفارش‌ها\n"
        "💰 مدیریت قیمت‌ها\n"
        "👥 کاربران\n"
        "📢 پیام همگانی\n"
        "━━━━━━━━━━━━━━\n\n"
        "مدیریت با موفقیت باز شد ✅",

        reply_markup=admin_menu()
    )


# تایید پرداخت

async def approve_order(
        callback: CallbackQuery,
        order_id: int
):

    if callback.from_user.id != ADMIN_ID:
        return


    waiting_configs[order_id] = True


    await callback.message.answer(

        "✅💳 پرداخت تایید شد\n\n"

        f"🆔 سفارش: #{order_id}\n\n"

        "📡 حالا کانفیگ مشتری را ارسال کن:\n\n"
        "مثال:\n"
        "vless://xxxx"

    )


# رد پرداخت

async def reject_order(
        callback: CallbackQuery,
        order_id: int
):

    if callback.from_user.id != ADMIN_ID:
        return


    await callback.message.answer(

        "❌ پرداخت رد شد\n\n"
        f"🆔 سفارش: #{order_id}"

    )


# دریافت کانفیگ از ادمین

async def receive_config(
        message: Message
):

    if message.from_user.id != ADMIN_ID:
        return


    if not waiting_configs:

        return


    order_id = list(waiting_configs.keys())[0]


    del waiting_configs[order_id]


    await message.answer(

        "🔥✅ کانفیگ دریافت شد\n\n"
        f"🆔 سفارش #{order_id}\n"
        "📤 آماده ارسال به مشتری"

    )
