from database import Order, async_session


# ساخت سفارش جدید

async def create_order(
    user_id,
    plan_id
):

    async with async_session() as session:

        order = Order(
            user_id=user_id,
            plan_id=plan_id,
            status="waiting",
            receipt="",
            config=""
        )

        session.add(order)

        await session.commit()

        return order.id



# ذخیره رسید پرداخت

async def save_receipt(
    order_id,
    receipt
):

    async with async_session() as session:

        order = await session.get(
            Order,
            order_id
        )

        if order:

            order.receipt = receipt
            order.status = "checking"

            await session.commit()



# تایید پرداخت

async def approve_order(
    order_id
):

    async with async_session() as session:

        order = await session.get(
            Order,
            order_id
        )

        if order:

            order.status = "approved"

            await session.commit()



# رد پرداخت

async def reject_order(
    order_id
):

    async with async_session() as session:

        order = await session.get(
            Order,
            order_id
        )

        if order:

            order.status = "rejected"

            await session.commit()



# ذخیره کانفیگ

async def save_config(
    order_id,
    config
):

    async with async_session() as session:

        order = await session.get(
            Order,
            order_id
        )

        if order:

            order.config = config
            order.status = "active"

            await session.commit()
