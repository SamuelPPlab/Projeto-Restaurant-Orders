import csv


def favorite(client, orders):
    asked_by_client = {}
    favorite_food = ""
    times_asked = 0
    for (name, food, _) in orders:
        if name == client:
            if food in asked_by_client:
                asked_by_client[food] += 1
            else:
                asked_by_client[food] = 1

            if asked_by_client[food] > times_asked:
                favorite_food = food
                times_asked = asked_by_client[food]
    return favorite_food


def many_times_asked(client, food, orders):
    times_asked = 0
    for (name, eat, _) in orders:
        if name == client and eat == food:
            times_asked += 1
    return times_asked


def never_asked(client, orders):
    asked_by_client = set()
    all_foods = set()
    for (name, food, _) in orders:
        all_foods.add(food)
        if name == client:
            asked_by_client.add(food)
    return all_foods.difference(asked_by_client)


def never_go_day(client, orders):
    days_client_go = set()
    all_days = set()
    for (name, _, day) in orders:
        all_days.add(day)
        if name == client:
            days_client_go.add(day)
    return all_days.difference(days_client_go)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    with open(path_to_file, mode='r') as csv_file:
        orders = list(csv.reader(csv_file, delimiter=","))
    with open("data/mkt_campaign.txt", "w") as log_file:
        log_file.write(f"{favorite('maria', orders)}\n")
        log_file.write(f"{many_times_asked('arnaldo','hamburguer',orders)}\n")
        log_file.write(f"{never_asked('joao', orders)}\n")
        log_file.write(f"{never_go_day('joao', orders)}\n")
