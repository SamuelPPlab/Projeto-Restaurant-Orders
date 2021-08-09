from csv import DictReader
from collections import Counter
import os


def read_data(path):
    if not path.endswith(".csv") or not os.path.isfile(path):
        raise FileNotFoundError(f"No such file or directory: '{path}'")
    with open(path, 'r') as csv_file:
        fieldnames = ['client', 'dish', 'day']
        reader = DictReader(csv_file, fieldnames=fieldnames)
        data = list(row for row in reader)
    return data


def most_eaten_dish_by_client(data, client):
    dish_list = []

    for item in data:
        if item['client'] == client:
            dish_list.append(item['dish'])

    most_eaten_dish, _ = Counter(dish_list).most_common()[0]
    return most_eaten_dish


def dish_quantity_by_client(data, client, dish):
    dish_list = []

    for item in data:
        if item['client'] == client:
            dish_list.append(item['dish'])

    dish_counter = dict(Counter(dish_list))
    return dish_counter.get(dish)


def never_ordered_dish_by_client(data, client):
    dishes = set()
    ordered_dish = set()

    for item in data:
        dishes.add(item['dish'])
        if item['client'] == client:
            ordered_dish.add(item['dish'])

    return dishes.difference(ordered_dish)


def days_without_visit_by_client(data, client):
    days = set()
    visit_days = set()

    for item in data:
        days.add(item['day'])
        if item['client'] == client:
            visit_days.add(item['day'])

    return days.difference(visit_days)


def analyze_log(path_to_file):
    data = read_data(path_to_file)
    maria_most_eaten_dish = most_eaten_dish_by_client(data, 'maria')
    arnaldo_dish_quantity = dish_quantity_by_client(
        data, 'arnaldo', 'hamburguer'
    )
    joao_never_ordered_dish = never_ordered_dish_by_client(data, 'joao')
    joao_days_without_visit = days_without_visit_by_client(data, 'joao')

    result = f"""{maria_most_eaten_dish}
{arnaldo_dish_quantity}
{joao_never_ordered_dish}
{joao_days_without_visit}"""

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(result)
