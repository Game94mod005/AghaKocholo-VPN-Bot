from aiogram.types import Message, CallbackQuery

from config import ADMIN_ID
from keyboards import admin_menu



async def open_admin(
    message: Message
):

    if message.from_user.id != ADMIN_ID:

        return


    await message.answer(

        "👑🔥 AghaKocholo Admin Panel\n\n"

        "📊 مدیریت کامل ربات\n"
        "━━━━━━━━━━━━\n"

        "🛒 سفارش‌ها\n"
        "💰 قیمت‌ها\n"
        "👥 کاربران\n"
        "📢 تبلیغات\n"

        ,

        reply_markup=admin_menu()

    )



async def admin_button(
    callback: CallbackQuery
):

    if callback.from_user.id != ADMIN_ID:

        await callback.answer(
            "❌ دسترسی ندارید"
        )

        return



    if callback.data == "admin_stats":

        await callback.message.answer(

            "📊 آمار ربات\n\n"

            "👥 کاربران: 0\n"
            "🛒 سفارش‌ها: 0\n"
            "💰 فروش: 0 تومان"

        )


    elif callback.data == "admin_prices":

        await callback.message.answer(

            "💰 مدیریت قیمت‌ها\n\n"

            "💎 Diamond\n"
            "5GB : 20000\n"
            "10GB : 40000\n"
            "15GB : 60000\n"
            "20GB : 80000\n\n"

            "👑 Gold\n"
            "5GB : 50000\n"
            "10GB : 100000"

        )


    await callback.answer()
