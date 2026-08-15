from aiogram.types import CallbackQuery, Message

from config import ADMIN_ID
from keyboards import admin_menu, receipt_buttons


async def open_admin(message: Message):

    if message.from_user.id != ADMIN_ID:
        return


    await message.answer(
        "👑🔥 AghaKocholo Admin Panel\n\n"

        "📊 داشبورد مدیریت\n"
        "━━━━━━━━━━━━\n"

        "🛒 سفارش‌ها\n"
        "💰 قیمت‌ها\n"
        "👥 کاربران\n"
        "📢 تبلیغات",

        reply_markup=admin_menu()
    )



async def admin_button(callback: CallbackQuery):

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
            "💰 فروش: 0 تومان\n\n"
            "🔥 سیستم فعال است"
        )


    elif callback.data == "admin_prices":

        await callback.message.answer(
            "💰 مدیریت قیمت\n\n"

            "💎 Diamond\n"
            "5GB : 20,000\n"
            "10GB : 40,000\n"
            "15GB : 60,000\n"
            "20GB : 80,000\n\n"

            "👑 Gold\n"
            "5GB : 50,000\n"
            "10GB : 100,000"
        )


    await callback.answer()
