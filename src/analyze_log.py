import csv
from collections import Counter


def most_requested_dish(orders, person):
    person_orders = list(map(lambda order: order[1], filter(
        lambda name: name[0] == person, orders)))
    return (Counter(person_orders).most_common(1))[0][0]


def how_many_times_was_requested(orders, person, dish):
    person_orders = list(filter(
        lambda name: name[0] == person and name[1] == dish, orders))
    print(len(person_orders))
    return len(person_orders)


def never_requested_dishes(orders, person):
    dishes = set([order[1] for order in orders])
    person_orders = set(list(map(lambda order: order[1], filter(
        lambda name: name[0] == person, orders))))
    return dishes.difference(person_orders)


def never_attended_days(orders, person):
    days = set([order[2] for order in orders])
    person_orders = set(list(map(lambda order: order[2], filter(
        lambda name: name[0] == person, orders))))
    return days.difference(person_orders)


def analyze_log(path_to_file):
    with open(path_to_file, mode="r") as file:
        orders = [row for row in csv.reader(file)]
        requested = most_requested_dish(orders, 'maria')
        times = how_many_times_was_requested(orders, 'arnaldo', 'hamburguer')
        never_requested = never_requested_dishes(orders, 'joao')
        never_attended = never_attended_days(orders, 'joao')

    with open("./data/mkt_campaign.txt", mode="w") as file:
        file.write(f'{requested}\n')
        file.write(f'{str(times)}\n')
        file.write(f'{str(never_requested)}\n')
        file.write(f'{str(never_attended)}\n')
