import csv


def most_frequent_item(list_dishes):
    quantity_dishes = dict()
    for item in list_dishes:
        quantity_dishes[item] = quantity_dishes.get(item, 0) + 1
    most_frequent_name = ""
    most_frequent_quantity = 0
    for dishe, quantity in quantity_dishes.items():
        if quantity > most_frequent_quantity:
            most_frequent_quantity = quantity
            most_frequent_name = dishe
    return most_frequent_name


def number_of_dishes_per_person(list_dishes, dishe):
    return list_dishes.count(dishe)


def dishes_never_ordered_per_person(menu, list_dishes):
    set_dishes = set(list_dishes)
    return menu.difference(set_dishes)


def days_person_not_go_cafeteria(days_of_week, list_days):
    set_days = set(list_days)
    return days_of_week.difference(set_days)


def read_csv_to_list(path_to_file):
    with open(path_to_file, "r") as file:
        reader = csv.reader(file)
        orders = [rows for rows in reader]
    return orders


def day_that_most_appears(every_days):
    return most_frequent_item(every_days)


def day_that_appears_less(every_days):
    quantity_dishes = dict()
    for item in every_days:
        quantity_dishes[item] = quantity_dishes.get(item, 0) + 1
    less_frequent_name = ''
    less_frequent_quantity = 1000
    for day, quantity in quantity_dishes.items():
        if quantity < less_frequent_quantity:
            less_frequent_quantity = quantity
            less_frequent_name = day
    return less_frequent_name
