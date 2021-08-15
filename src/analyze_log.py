import operator
import csv


def count_freq_order_numb(my_list_orders, order_item):
    order_quantity = {}
    for item in my_list_orders:
        if (item == order_item):
            if (item in order_quantity):
                order_quantity[item] += 1
            else:
                order_quantity[item] = 1

    return order_quantity[order_item]


def count_frequency_order_by_name(my_list_orders):
    frequency_orders = {}
    for item in my_list_orders:
        if (item in frequency_orders):
            frequency_orders[item] += 1
        else:
            frequency_orders[item] = 1
    return max(frequency_orders.items(), key=operator.itemgetter(1))[0]


def items_never_ordered(data_orders, name_client):
    history_client = set()
    items_menu = set()

    for order in data_orders:
        items_menu.add(order['order'])

    for order in data_orders:
        if order["name"] == name_client:
            history_client.add(order["order"])
    return set(items_menu) - set(history_client)


def which_days_not_snack_bar(data, client_name):
    days_week = set()
    days_in_snack_bar = set()
    for days in data:
        days_week.add(days['day'])
    for days in data:
        if days["name"] == client_name:
            days_in_snack_bar.add(days["day"])
    return set(days_week) - set(days_in_snack_bar)


def customer_history(data_orders, client_name):
    list_order_client = []
    for order in data_orders:
        if(order['name'] == client_name):
            list_order_client.append(order['order'])
    return list_order_client


def analyze_log(path_to_file):
    with open(path_to_file, mode="r") as res:
        orders = list(csv.DictReader(res, fieldnames=["name", "order", "day"]))
    return orders
    h_customer_maria = customer_history(orders, 'maria')
    most_req_maria = count_frequency_order_by_name(h_customer_maria)

    h_customer_arnaldo = customer_history(orders, 'arnaldo')
    most_req_arnaldo = count_freq_order_numb(h_customer_arnaldo, 'hamburguer')

    itens_never_ordered_joao = items_never_ordered(orders, 'joao')

    days_joao_attends = which_days_not_snack_bar(orders, 'joao')

    with open("data/mkt_campaign.txt", "w") as txt:
        txt.write(
            f"{most_req_maria}\n"
            f"{most_req_arnaldo}\n"
            f"{itens_never_ordered_joao}\n"
            f"{days_joao_attends}\n"
        )
