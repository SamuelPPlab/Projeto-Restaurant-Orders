import csv
from collections import Counter


def read_csv(path_to_file):
    with open(path_to_file, "r") as file:
        return list(csv.reader(file))


def quantity_ordered(name, meal, orders):
    counter = 0
    for item in orders:
        if item[0] == name and item[1] == meal:
            counter += 1
    return counter


def favorite(name, orders):
    client_orders = []
    if len(orders) > 0:
        for item in orders:
            if item[0] == name:
                client_orders.append(item[1])
        fav = Counter(client_orders).most_common(1)[0][0]
        return fav


def days_never_order(name, days):
    all_days = set()
    client_days = set()
    for day in days:
        all_days.add(day[2])
    for client in days:
        if client[0] == name:
            client_days.add(client[2])
    return all_days.difference(client_days)


def meals_never_order(name, orders):
    all_meals = set()
    client_meal = set()
    for item in orders:
        all_meals.add(item[1])
    for item in orders:
        if item[0] == name:
            client_meal.add(item[1])
    return all_meals.difference(client_meal)


def analyze_log(path_to_file):
    result = ""
    data = read_csv(path_to_file)
    fav = favorite("maria", data)
    times = quantity_ordered("arnaldo", "hamburguer", data)
    not_ordered = meals_never_order("joao", data)
    days = days_never_order("joao", data)
    result = f"{fav}\n{times}\n{not_ordered}\n{days}"
    f = open("data/mkt_campaign.txt", "w")
    f.write(result)
    f.close()
