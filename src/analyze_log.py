import csv
from collections import Counter


def read_csv(filepath):
    with open(filepath) as file:
        fieldnames = ["name", "order", "week_day"]
        reader = csv.DictReader(file, fieldnames=fieldnames)
        return [data for data in reader]


def most_frequent_dish(orders, person):
    order_filter = [item["order"] for item in orders if item["name"] in person]
    dish_count = Counter(order_filter)
    return max(dish_count, key=dish_count.get)


def count_ordered_dish(orders, person, dish):
    order_filter = [item["order"] for item in orders if item["name"] in person]
    dish_count = Counter(order_filter)
    return dish_count[dish]


def dishes_never_ordered(orders, person):
    orders_set = set(item["order"] for item in orders)
    set_filter = set(
      [item["order"] for item in orders if item["name"] in person])
    return orders_set - set_filter


def days_not_visited(orders, person):
    orders_set = set(item["week_day"] for item in orders)
    set_filter = set(
      [item["week_day"] for item in orders if item["name"] in person])
    return orders_set - set_filter


def analyze_log(path_to_file):
    orders = read_csv(path_to_file)
    frequent_dish = most_frequent_dish(orders, "maria")
    count_dish = count_ordered_dish(orders, "arnaldo", "hamburguer")
    dishes_not_ordered = dishes_never_ordered(orders, "joao")
    days_without_visit = days_not_visited(orders, "joao")
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{frequent_dish}\n"
            f"{count_dish}\n"
            f"{dishes_not_ordered}\n"
            f"{days_without_visit}"
        )
