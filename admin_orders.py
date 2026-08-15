from aiogram.types import Message

from config import ADMIN_ID

from orders import (
    approve_order,
    reject_order,
    save_config
)


# تایید پرداخت

async def approve_payment(
    callback,
    order_id
):

    if callback.from_user.id != ADMIN_ID:
        return


    await approve_order(order_id)


    await callback.message.answer(
        "✅ پرداخت تایید شد\n\n"
        "📩 حالا کانفیگ را ارسال کنید."
    )



# رد پرداخت

async def reject_payment(
    callback,
    order_id
):

    if callback.from_user.id != ADMIN_ID:
        return


    await reject_order(order_id)


    await callback.message.answer(
        "❌ پرداخت رد شد."
    )



# دریافت کانفیگ از ادمین

async def receive_config(
    message: Message,
    order_id
):

    if message.from_user.id != ADMIN_ID:
        return


    await save_config(
        order_id,
        message.text
    )


    await message.answer(
        "🔥 کانفیگ ذخیره شد و برای مشتری ارسال می‌شود."
    )
