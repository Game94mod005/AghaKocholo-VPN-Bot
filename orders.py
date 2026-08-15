from database import async_session, Order
from sqlalchemy import select


async def create_order(
    user_id,
    plan_name,
    price
):

    async with async_session() as session:

        order = Order(
            user_id=user_id,
            plan_id=0,
            status="waiting_receipt",
            receipt="",
            config=""
        )

        session.add(order)

        await session.commit()

        await session.refresh(order)

        return order.id



async def add_receipt(
    order_id,
    receipt_id
):

    async with async_session() as session:

        order = await session.get(
            Order,
            order_id
        )

        if order:

            order.receipt = receipt_id
            order.status = "checking"

            await session.commit()



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
