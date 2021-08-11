import csv
from collections import Counter


# Qual o prato mais pedido por 'maria'?


def most_ordered_dish_by_name(name, dish_list):
    count_dish = {}
    for order in dish_list:
        if order[0] == name:
            if order[1] not in count_dish:
                count_dish[order[1]] = 1
            else:
                count_dish[order[1]] += 1

    most_ordered = Counter(count_dish).most_common(1)[0][0]
    return most_ordered


# Quantas vezes 'arnaldo' pediu 'hamburguer'?


def times_a_dish_was_ordered(name, dish_name, dish_list):
    count_dish = {}
    for order in dish_list:
        if order[0] == name and order[1] == dish_name:
            if order[1] not in count_dish:
                count_dish[order[1]] = 1
            else:
                count_dish[order[1]] += 1

    most_ordered = Counter(count_dish).most_common(1)[0][1]
    return most_ordered


# Quais pratos 'joao' nunca pediu?


def all_dishes(dish_list):
    all_dishes = []
    for order in dish_list:
        if order[1] not in all_dishes:
            all_dishes.append(order[1])
    return all_dishes


def not_ordered_dish(name, dish_list):
    count_dish = {}
    all_ordered_dishes = all_dishes(dish_list)

    for order in dish_list:
        if order[0] == name:
            if order[1] not in count_dish:
                count_dish[order[1]] = 1
            else:
                count_dish[order[1]] += 1

    counted_dish = set(count_dish)
    all_ordered = set(all_ordered_dishes)

    return all_ordered.difference(counted_dish)


# Quais dias 'joao' nunca foi na lanchonete?


def every_day_of_the_week(dish_list):
    all_days = []
    for order in dish_list:
        if order[2] not in all_days:
            all_days.append(order[2])
    return all_days


def days_not_attended(name, dish_list):
    days_attended = []
    all_days_of_the_week = every_day_of_the_week(dish_list)

    for order in dish_list:
        if order[0] == name:
            if order[2] not in days_attended:
                days_attended.append(order[2])

    all_days_csv_file = set(all_days_of_the_week)
    days_attended_by_name = set(days_attended)

    return all_days_csv_file.difference(days_attended_by_name)


def analyze_log(path_to_file):
    isTrue = path_to_file.endswith(".csv")
    if isTrue:
        with open(path_to_file) as file:
            csv_file = list(csv.reader(file))
            most_ordered = most_ordered_dish_by_name("maria", csv_file)
            most_ordered_dish_by_name_and_dish = times_a_dish_was_ordered(
                "arnaldo", "hamburguer", csv_file
            )
            not_ordered = not_ordered_dish("joao", csv_file)
            not_attended = days_not_attended("joao", csv_file)

            report = (
                f"{most_ordered}\n"
                f"{most_ordered_dish_by_name_and_dish}\n"
                f"{not_ordered}\n"
                f"{not_attended}"
            )
        with open("data/mkt_campaign.txt", "w") as file:
            file.write(report)

            return report
    else:
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
