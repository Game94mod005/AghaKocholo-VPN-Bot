from config import ADMIN_ID


# ذخیره سفارش‌هایی که منتظر کانفیگ هستند
waiting_config = {}


def set_waiting_config(order_id, user_id):

    waiting_config[order_id] = user_id



def get_user_by_order(order_id):

    return waiting_config.get(order_id)



def remove_order(order_id):

    if order_id in waiting_config:
        del waiting_config[order_id]
