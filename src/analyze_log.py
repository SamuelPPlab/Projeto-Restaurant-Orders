import csv
from collections import Counter


def most_requested_dish(orders, person):
    o_list = [order[1] for order in orders if order[0] == person]
    return (Counter(o_list).most_common(1))[0][0]


def how_many_times_was_requested(orders, person, dish):
    o_list = list(filter(
        lambda name: name[0] == person and name[1] == dish, orders))
    return len(o_list)


def never_requested_dishes(orders, person):
    dishes = [order[1] for order in orders]
    o_list = [order[1] for order in orders if order[0] == person]
    return (set(dishes)).difference(set(o_list))


def never_attended_days(orders, person):
    days = [order[2] for order in orders]
    o_list = [order[2] for order in orders if order[0] == person]
    return (set(days)).difference(set(o_list))


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
