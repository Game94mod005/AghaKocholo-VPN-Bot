from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛒 خرید VPN",
                    callback_data="buy"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📦 سرویس‌های من",
                    callback_data="services"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔄 تمدید سرویس",
                    callback_data="renew"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🆘 پشتیبانی",
                    callback_data="support"
                )
            ]
        ]
    )


def admin_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📊 آمار",
                    callback_data="stats"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🛒 سفارش‌ها",
                    callback_data="orders"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👥 کاربران",
                    callback_data="users"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📢 پیام همگانی",
                    callback_data="broadcast"
                )
            ]
        ]
    )
