import csv


def most_requested_dish(orders_csv, client):
    orders = {}
    for client_name, client_dish, day in orders_csv:
        if client_name == client:
            if client_dish in orders_csv:
                orders[client_dish] += 1
            else:
                orders[client_dish] = 1
    return max(orders, key=orders.get)


def count_client_dish(orders_csv, client, dish):
    counter = 0
    for client_name, client_dish, day in orders_csv:
        if client_name == client and client_dish == dish:
            counter += 1
    return counter


def dishes_never_ordered_by_client(orders_csv, client):
    all_dishes = set()
    client_dishes = set()
    for client_dish in orders_csv:
        all_dishes.add(client_dish[1])
        if client_dish[0] == client:
            client_dishes.add(client_dish[1])
    return all_dishes.difference(client_dishes)


def days_never_visited_by_client(orders_csv, client):
    all_days = set()
    client_days = set()
    for client_day in orders_csv:
        all_days.add(client_day[2])
        if client_day[0] == client:
            client_days.add(client_day[2])
    return all_days.difference(client_days)


def read_orders_csv(path_to_file):
    try:
        return list(csv.reader(open(path_to_file)))
    except ValueError:
        return f"No such file or directory: '{path_to_file}'"


def analyze_log(path_to_file):
    file_read = read_orders_csv(path_to_file)
    most_requested = most_requested_dish(file_read, 'maria')
    count_dish = count_client_dish(file_read, 'arnaldo', 'hamburguer')
    dishes_never_ordered = dishes_never_ordered_by_client(file_read, 'joao')
    days_never_visited = days_never_visited_by_client(file_read, 'joao')

    campaign_log_file = open("data/mkt_campaign.txt", "w")

    campaign_log_file.write(f"{most_requested}\n")
    campaign_log_file.write(f"{count_dish}\n")
    campaign_log_file.write(f"{dishes_never_ordered}\n")
    campaign_log_file.write(f"{days_never_visited}")
