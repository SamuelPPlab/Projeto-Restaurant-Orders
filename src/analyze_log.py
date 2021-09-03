import csv


def open_csv(path):
    fileData = []

    with open(path) as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            fileData.append(row)

    return fileData


def write_file(str):
    with open('data/mkt_campaign.txt', mode='w') as file:
        file.writelines(str)


def get_favorite_order(data, customer):
    meals = {}
    for order in data:
        if customer in order:
            if order[1] not in meals:
                meals[order[1]] = 1
            else:
                meals[order[1]] += 1

    return max(meals, key=meals.get)


def get_order_quantity(data, customer, order_item):
    meals = {}
    for order in data:
        if customer in order:
            if order[1] not in meals:
                meals[order[1]] = 1
            else:
                meals[order[1]] += 1

    if order_item in meals:
        return meals[order_item]

    return 0


def get_never_ordered_items(data, customer):
    meals = set()
    customerOrdered = set()
    for order in data:
        meals.add(order[1])
        if customer in order:
            customerOrdered.add(order[1])

    return meals.difference(customerOrdered)


def get_never_visited_days(data, customer):
    week = set()
    customerVisited = set()
    for order in data:
        week.add(order[2])
        if customer in order:
            customerVisited.add(order[2])

    return week.difference(customerVisited)


def analyze_log(path):
    fileData = []

    fileData = open_csv(path)

    str = "{0}\n{1}\n{2}\n{3}".format(
        get_favorite_order(fileData, 'maria'),
        get_order_quantity(fileData, 'arnaldo', 'hamburguer'),
        get_never_ordered_items(fileData, 'joao'),
        get_never_visited_days(fileData, 'joao')
    )

    write_file(str)


analyze_log('data/orders_1.csv')
