from csv import DictReader
from collections import Counter


def analyze_log(path_to_file):
    with open(path_to_file, mode="r") as res:
        data = list(
            DictReader(res, fieldnames=["name", "meal", "day"])
        )

    with open("data/mkt_campaign.txt", "w") as txt:
        txt.write(
            f"{maria_favorite_meal(data)}\n"
            f"{how_many_times_did_arnaldo_order_a_hamburger(data)}\n"
            f"{joao_never_ordered_meals(data)}\n"
            f"{days_joao_didnt_go(data)}\n"
        )


def maria_favorite_meal(data):
    maria_orders = []
    for order in data:
        if order["name"] == "maria":
            maria_orders.append(order["meal"])
    return Counter(maria_orders).most_common(1)[0][0]


def how_many_times_did_arnaldo_order_a_hamburger(data):
    hamburguers = 0
    for order in data:
        if order["name"] == "arnaldo" and order["meal"] == "hamburguer":
            hamburguers += 1
    return hamburguers


def joao_never_ordered_meals(data):
    joao_meals = set()
    all_meals = set()
    for order in data:
        all_meals.add(order["meal"])
        if(order["name"] == "joao"):
            joao_meals.add(order["meal"])
    return all_meals.difference(joao_meals)


def days_joao_didnt_go(data):
    joao_days = set()
    days = set()
    for order in data:
        days.add(order["day"])
        if order["name"] == "joao":
            joao_days.add(order["day"])
    return days.difference(joao_days)
