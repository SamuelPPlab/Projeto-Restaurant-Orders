import csv


def most_requested_dish(orders_csv, costumer):
    orders = {}
    for costumer_name, costumer_dish, day in orders_csv:
        if costumer_name == costumer:
            if costumer_dish in orders_csv:
                orders[costumer_dish] += 1
            else:
                orders[costumer_dish] = 1
    return max(orders, key=orders.get)


def count_costumer_dish(orders_csv, costumer, dish):
    counter = 0
    for costumer_name, costumer_dish, day in orders_csv:
        if costumer_name == costumer and costumer_dish == dish:
            counter += 1
    return counter


def dishes_never_ordered_by_costumer(orders_csv, costumer):
    all_dishes = set()
    costumer_dishes = set()
    for costumer_dish in orders_csv:
        all_dishes.add(costumer_dish[1])
        if costumer_dish[0] == costumer:
            costumer_dishes.add(costumer_dish[1])
    return all_dishes.difference(costumer_dishes)


def days_never_visited_by_costumer(orders_csv, costumer):
    all_days = set()
    costumer_days = set()
    for costumer_day in orders_csv:
        all_days.add(costumer_day[2])
        if costumer_day[0] == costumer:
            costumer_days.add(costumer_day[2])
    return all_days.difference(costumer_days)


def read_orders_csv(path_to_file):
    try:
        return list(csv.reader(open(path_to_file)))
    except ValueError:
        return f"No such file or directory: '{path_to_file}'"


def analyze_log(path_to_file):
    file_read = read_orders_csv(path_to_file)
    most_requested = most_requested_dish(file_read, 'maria')
    count_dish = count_costumer_dish(file_read, 'arnaldo', 'hamburguer')
    dishes_never_ordered = dishes_never_ordered_by_costumer(file_read, 'joao')
    days_never_visited = days_never_visited_by_costumer(file_read, 'joao')

    campaign_log_file = open("data/mkt_campaign.txt", "w")

    campaign_log_file.write(f"{most_requested}\n")
    campaign_log_file.write(f"{count_dish}\n")
    campaign_log_file.write(f"{dishes_never_ordered}\n")
    campaign_log_file.write(f"{days_never_visited}")
