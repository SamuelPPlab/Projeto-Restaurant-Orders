import csv
from collections import Counter
import operator


def get_most_ordered(person_name, order_list):
    customer_orders = list()
    for order in order_list:
        if order["name"] == person_name:
            customer_orders.append(order["meal"])
    orders_counted = Counter(customer_orders)
    # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    most_ordered = max(orders_counted, key=orders_counted.get)
    return most_ordered


def count_meal(person_name, meal_name, order_list):
    customer_orders = list()
    for order in order_list:
        if order["name"] == person_name:
            customer_orders.append(order["meal"])
    orders_counted = Counter(customer_orders)
    print(orders_counted)
    return orders_counted[meal_name]


def never_ordered(person_name, order_list):
    customer_orders = list()
    never_ordered_list = list()
    meal_options = ["coxinha", "hamburguer", "misto-quente", "pizza"]

    for order in order_list:
        if order["name"] == person_name:
            customer_orders.append(order["meal"])
    for meal_option in meal_options:
        if meal_option not in customer_orders:
            never_ordered_list.append(meal_option)

    return set(never_ordered_list)


def never_going(person_name, order_list):
    days_orders = list()
    never_going_days_list = list()
    days_options = ["sabado", "segunda-feira", "terça-feira"]

    for order in order_list:
        if order["name"] == person_name:
            days_orders.append(order["day"])
    for meal_option in days_options:
        if meal_option not in days_orders:
            never_going_days_list.append(meal_option)
    return set(never_going_days_list)


def analyze_log(path_to_file):
    file_obj = csv.DictReader(open(path_to_file), fieldnames=[
                              'name', 'meal', 'day'])
    orders_list = list()
    for order in file_obj:
        orders_list.append(order)

    maria_most_ordered = get_most_ordered("maria", file_obj)
    arnaldo_hamburguer_count = count_meal("arnaldo", "hamburguer", file_obj)
    joao_never_order = never_ordered("joao", file_obj)
    joao_never_going = never_going("joao", file_obj)
    file = "data/mkt_campaign.txt"
    text = [
        f"{maria_most_ordered}\n",
        f"{arnaldo_hamburguer_count}\n",
        f"{joao_never_order}\n",
        f"{joao_never_going}\n",
    ]
    with open(file, "w") as f:
        f.writelines(text)
