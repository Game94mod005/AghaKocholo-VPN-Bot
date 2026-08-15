from plans import DIAMOND_PLANS, GOLD_PLANS


# حالت انتظار گرفتن قیمت جدید
waiting_price = {}


def request_price_change(user_id, plan):

    waiting_price[user_id] = plan



def save_new_price(user_id, price):

    if user_id not in waiting_price:
        return False


    plan = waiting_price[user_id]


    price = int(price)


    if plan in DIAMOND_PLANS:

        DIAMOND_PLANS[plan] = price


    elif plan in GOLD_PLANS:

        GOLD_PLANS[plan] = price


    del waiting_price[user_id]


    return True
