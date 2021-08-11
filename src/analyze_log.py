import csv


def days_requested(name, path_to_file):
    with open(path_to_file) as file:
        requests = csv.reader(file)
        days_requested = {}
        for row in requests:
            if row[0] == name:
                if row[2] in days_requested:
                    days_requested[row[2]] += 1
                else:
                    days_requested[row[2]] = 1
        return days_requested


def food_requested(name, path_to_file):
    with open(path_to_file) as file:
        requests = csv.reader(file)
        food_requested = {}
        for row in requests:
            if row[0] == name:
                if row[1] in food_requested:
                    food_requested[row[1]] += 1
                else:
                    food_requested[row[1]] = 1
        return food_requested


def get_menu(path_to_file):
    with open(path_to_file) as file:
        requests = csv.reader(file)
        menu = set()
        for row in requests:
            if row[1] not in menu:
                menu.add(row[1])
        return menu


def get_days(path_to_file):
    with open(path_to_file) as file:
        requests = csv.reader(file)
        days = set()
        for row in requests:
            if row[2] not in days:
                days.add(row[2])
        return days


def more_requested_by(name, food, path_to_file):
    food = food_requested(name, path_to_file)
    # Encontrei a função max em uma busca no stackoverflow:
    # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    return max(food, key=food.get)


def never_request(name, path_to_file):
    food = food_requested(name, path_to_file)
    menu = get_menu(path_to_file)
    food_never_requested = set()
    for item in menu:
        if item not in food:
            food_never_requested.add(item)
    return food_never_requested


def day_never_request(name, path_to_file):
    day_with_requests = days_requested(name, path_to_file)
    days = get_days(path_to_file)
    days_never_requested = set()
    for day in days:
        if day not in day_with_requests:
            days_never_requested.add(day)
    return days_never_requested


def count_by_food(name, food, path_to_file):
    food_list = food_requested(name, path_to_file)
    return food_list[food]


def analyze_log(path_to_file):
    most_requested = more_requested_by("maria", "", path_to_file)
    count_requests_by_food = count_by_food(
        "arnaldo", "hamburguer", path_to_file
    )
    food_never_requested = never_request("joao", path_to_file)
    days_never_requested = day_never_request("joao", path_to_file)

    with open("data/mkt_campaign.txt", mode="w+") as file:
        file.write(f"{most_requested}\n")
        file.write(f"{str(count_requests_by_food)}\n")
        file.write(f"{str(food_never_requested)}\n")
        file.write(f"{str(days_never_requested)}\n")


analyze_log("data/orders_1.csv")
