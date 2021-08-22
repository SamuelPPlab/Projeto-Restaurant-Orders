import csv
from collections import Counter

def most_demanded_by_client(name, list_orders):
    orders = []
    for element in list_orders:
        if element['client'] == name:
            orders.append(element['order'])
    counter = Counter(orders)
    return list(counter.keys())[0]

def quantity_order(name, order, list_orders):
    c = 0
    for element in list_orders:
        if element['client'] == name and element['order'] == order:
            c = c + 1
    return c

def orders_never_ordered(name, list_orders):
    orders_already_ordered = set()
    all_orders = set()
    for element in list_orders:
        all_orders.add(element['order'])
        if element['client'] == name:
            orders_already_ordered.add(element['order'])
    return all_orders.difference(orders_already_ordered)

def days_never_gone(name, list_orders):
    days_already_done = set()
    all_days = set()
    for element in list_orders:
        all_days.add(element['day'])
        if element['client'] == name:
            days_already_done.add(element['day'])
    return all_days.difference(days_already_done)

def analyze_log(path_to_file):
    if path_to_file.endswith('.csv'):
        with open(path_to_file, 'r') as csv_file:
            array = []
            data = csv.DictReader(csv_file, ['client', 'order', 'day'])
            for element in data:
                array.append(element)
            result_array = [
                f"{most_demanded_by_client('maria', array)}\n",
                f"{quantity_order('arnaldo', 'hamburguer', array)}\n",
                f"{orders_never_ordered('joao', array)}\n",
                f"{days_never_gone('joao', array)}",
            ]
        with open("data/mkt_campaign.txt", 'w') as file:
            file.writelines(result_array)
    else:
        raise FileNotFoundError()
