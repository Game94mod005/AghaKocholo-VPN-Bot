from aiogram.types import Message, CallbackQuery

from config import ADMIN_ID
from keyboards import admin_menu

from config_sender import (
    set_waiting_config,
    get_user_by_order,
    remove_order
)

from orders import save_config


async def open_admin(message: Message):

    if message.from_user.id != ADMIN_ID:
        return


    await message.answer(
        "👑🔥 AghaKocholo Admin\n\n"
        "مدیریت کامل ربات فعال است 🚀",

        reply_markup=admin_menu()
    )



async def approve_payment(callback, order_id):

    if callback.from_user.id != ADMIN_ID:
        return


    # اینجا بعداً از دیتابیس کاربر را می‌گیریم

    await callback.message.answer(

        "✅ پرداخت تایید شد\n\n"
        "📡 حالا کانفیگ را ارسال کنید:\n"
        "مثال:\n"
        "vless://xxxx"

    )


    set_waiting_config(
        order_id,
        callback.from_user.id
    )



async def receive_config(message: Message):

    if message.from_user.id != ADMIN_ID:
        return


    for order_id,user_id in list(waiting_config.items()):

        await message.bot.send_message(
            user_id,

            "🎉🔥 سرویس شما فعال شد\n\n"
            "🔗 کانفیگ شما:\n\n"
            f"{message.text}\n\n"
            "⏳ اعتبار: 30 روز\n\n"
            "❤️ ممنون از خرید شما"

        )

        remove_order(order_id)

        break
