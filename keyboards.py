from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# 🏠 منوی اصلی کاربر

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
                    text="📚 آموزش اتصال",
                    callback_data="guide"
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


# 🌍 انتخاب لوکیشن

def locations():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="🇩🇪 آلمان",
                    callback_data="loc_Germany"
                ),

                InlineKeyboardButton(
                    text="🇹🇷 ترکیه",
                    callback_data="loc_Turkey"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🇫🇮 فنلاند",
                    callback_data="loc_Finland"
                ),

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


# 📦 حجم ها

def volumes():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="5GB 💾",
                    callback_data="vol_5"
                )
            ],

            [
                InlineKeyboardButton(
                    text="10GB 💾",
                    callback_data="vol_10"
                )
            ],

            [
                InlineKeyboardButton(
                    text="15GB 💾",
                    callback_data="vol_15"
                )
            ],

            [
                InlineKeyboardButton(
                    text="20GB 🚀",
                    callback_data="vol_20"
                )
            ]

        ]
    )


# 👑 پنل ادمین

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
                    text="💰 مدیریت قیمت",
                    callback_data="admin_prices"
                )
            ],

            [
                InlineKeyboardButton(
                    text="👥 کاربران",
                    callback_data="admin_users"
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
