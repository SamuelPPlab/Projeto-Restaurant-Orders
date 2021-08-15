import csv
from collections import Counter


def csv_reader(path_to_file):
    with open(path_to_file) as file:
        return list(csv.reader(file))


def favorite_meal_by_client(client_name, orders):
    client_orders = []
    for order in orders:
        if order[0] == client_name:
            client_orders.append(order[1])
    favorite_meal = Counter(client_orders).most_common(1)[0][0]
    return favorite_meal


def order_count(client_name, meal, orders):
    count = 0
    for order in orders:
        if order[0] == client_name and order[1] == meal:
            count += 1
    return count


def not_ordered(client_name, orders):
    all_meals = set()
    meal = set()
    for order in orders:
        all_meals.add(order[1])
    for order in orders:
        if order[0] == client_name:
            meal.add(order[1])

    return all_meals.difference(meal)


def days_without_order(client_name, days):
    all_days = set()
    client_days = set()
    for day in days:
        all_days.add(day[2])
    for client in days:
        if client[0] == client_name:
            client_days.add(client[2])
    return all_days.difference(client_days)


def analyze_log(path_to_file):
    data = csv_reader(path_to_file)

    report = (
        f"{favorite_meal_by_client('maria', data)}\n"
        f"{order_count('arnaldo', 'hamburguer', data)}\n"
        f"{not_ordered('joao', data)}\n"
        f"{days_without_order('joao', data)}"
    )

    f = open("data/mkt_campaign.txt", "w")
    f.write(report)
    f.close()
