from plans import DIAMOND_PLANS, GOLD_PLANS


# ذخیره انتخاب کاربر

user_orders = {}


def set_location(user_id, location):

    if user_id not in user_orders:
        user_orders[user_id] = {}

    user_orders[user_id]["location"] = location



def set_plan(user_id, plan):

    if user_id not in user_orders:
        user_orders[user_id] = {}

    user_orders[user_id]["plan"] = plan



def get_price(user_id):

    data = user_orders.get(user_id)

    if not data:
        return 0


    volume = data["plan"]


    if data.get("type") == "gold":

        return GOLD_PLANS.get(
            volume,
            0
        )


    return DIAMOND_PLANS.get(
        volume,
        0
    )



def get_order(user_id):

    return user_orders.get(
        user_id,
        {}
    )
