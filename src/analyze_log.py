import csv
import errno
import os


def handle_favorite(client, orders):
    most_asked_by_client = {}
    favorite_dish = ""
    times_asked = 0
    for (name, food, _) in orders:
        if name == client:
            if food in most_asked_by_client:
                most_asked_by_client[food] += 1
            else:
                most_asked_by_client[food] = 1
            if most_asked_by_client[food] > times_asked:
                favorite_dish = food
                times_asked = most_asked_by_client[food]
    return favorite_dish


def handle_most_asked(client, food, orders):
    times_asked = 0
    for (name, eat, _) in orders:
        if name == client and eat == food:
            times_asked += 1
    return times_asked


def handle_less_asked(client, orders):
    dishes_asked_by_client = set()
    dishes = set()
    for (name, food, _) in orders:
        dishes.add(food)
        if name == client:
            dishes_asked_by_client.add(food)
    return dishes.difference(dishes_asked_by_client)


def handle_not_show_up_day(client, orders):
    days_show_up = set()
    week = set()
    for (name, _, day) in orders:
        week.add(day)
        if name == client:
            days_show_up.add(day)
    return week.difference(days_show_up)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), path_to_file)
    with open(path_to_file, mode='r') as csv_file:
        orders = list(csv.reader(csv_file, delimiter=","))
    with open("data/mkt_campaign.txt", "w") as log_file:
        log_file.write(f"{handle_favorite('maria', orders)}\n")
        log_file.write(f"{handle_most_asked('arnaldo', 'hamburguer', orders)}\n")
        log_file.write(f"{handle_less_asked('joao', orders)}\n")
        log_file.write(f"{handle_not_show_up_day('joao', orders)}\n")