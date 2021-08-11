import csv


def file(path_to_file):
    restaurant_data = []

    with open(path_to_file, 'r') as file:
        reader = csv.DictReader(
            file, fieldnames=['name', 'food', 'date']
        )

        for row in reader:
            restaurant_data.append(row)

    return restaurant_data


def fav_dish(name, restaurant_data):
    orders = [
        data['food']
        for data in restaurant_data
        if data['name'] == name
    ]

    favorites = max(orders, key=orders.count)

    return favorites


def counter(name, food, restaurant_data):
    orders = [
        data['food'] for data in restaurant_data
        if data['name'] == name
        and data['food'] == food
    ]

    return len(orders)


def not_popular(name, tab, restaurant_data):
    menu = set([data[tab] for data in restaurant_data])

    popular = set([
        data[tab]
        for data in restaurant_data
        if data['name'] == name
    ])

    not_popular = menu.difference(popular)

    return not_popular


def marketing_data(content, path_to_file):
    with open(path_to_file, "w") as file:
        file.write(content)


def analyze_log(path_to_file):
    restaurant_data = file(path_to_file)

    content = (
        f"{fav_dish('maria', restaurant_data)}\n"
        f"{counter('arnaldo', 'hamburguer', restaurant_data)}\n"
        f"{not_popular('joao', 'food', restaurant_data)}\n"
        f"{not_popular('joao', 'date', restaurant_data)}"
    )

    marketing_data(content, './data/mkt_campaign.txt')
