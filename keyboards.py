from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💎 خرید پلن الماس",
                    callback_data="diamond"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👑 خرید پلن طلایی",
                    callback_data="gold"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📦 سرویس‌های من",
                    callback_data="my_services"
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


def locations():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🇩🇪 آلمان",
                    callback_data="loc_Germany"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🇹🇷 ترکیه",
                    callback_data="loc_Turkey"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🇫🇮 فنلاند",
                    callback_data="loc_Finland"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🇳🇱 هلند",
                    callback_data="loc_Netherlands"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🇺🇸 آمریکا",
                    callback_data="loc_USA"
                )
            ]
        ]
    )


def volumes():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="5GB 💾",
                    callback_data="vol_5"
                ),
                InlineKeyboardButton(
                    text="10GB 💾",
                    callback_data="vol_10"
                )
            ],
            [
                InlineKeyboardButton(
                    text="15GB 💾",
                    callback_data="vol_15"
                ),
                InlineKeyboardButton(
                    text="20GB 🚀",
                    callback_data="vol_20"
                )
            ]
        ]
    )


# دکمه های رسید

def receipt_buttons(order_id):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ تایید پرداخت",
                    callback_data=f"approve_{order_id}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="❌ رد پرداخت",
                    callback_data=f"reject_{order_id}"
                )
            ]
        ]
    )


# پنل ادمین

def admin_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📊 آمار",
                    callback_data="admin_stats"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🛒 سفارش‌ها",
                    callback_data="admin_orders"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💰 تغییر قیمت",
                    callback_data="admin_prices"
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
