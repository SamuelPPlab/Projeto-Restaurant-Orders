import csv
from collections import Counter


def most_ordered_food_by_client(data, name):
    orders = []

    for item in data:
        if item['client'] == name:
            orders.append(item['food'])

    counter = Counter(orders)
    return list(counter.keys())[0]


def food_counter(data, name, food):
    food_ordered = 0

    for element in data:
        if element['client'] == name and element['food'] == food:
            food_ordered = food_ordered + 1

    return food_ordered


def food_never_ordered(data, name):
    all_foods = set(order["food"] for order in data)

    foods_ordered = set(
        order["food"] for order in data
        if order["client"] == name
    )

    return all_foods.difference(foods_ordered)


def days_without_visit(data, name):
    all_days = set(order["day"] for order in data)

    days_visited = set(
        order["day"] for order in data
        if order["client"] == name
    )

    return all_days.difference(days_visited)


def analyze_log(path_to_file):
    with open(path_to_file) as csv_file:
        reader_file = csv.DictReader(csv_file, ['client', 'food', 'day'])
        data = list(row for row in reader_file)

        result = [
            f"{most_ordered_food_by_client(data, 'maria')}\n",
            f"{food_counter(data, 'arnaldo', 'hamburguer')}\n",
            f"{food_never_ordered(data, 'joao')}\n",
            f"{days_without_visit(data, 'joao')}\n"
        ]

    with open("./data/mkt_campaign.txt", 'w') as file:
        file.writelines(result)
