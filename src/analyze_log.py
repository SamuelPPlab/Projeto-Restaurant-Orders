import csv


def read_file_to_dictionary(path_to_file):
    file_type = path_to_file.split(".")[1]
    if file_type == "csv":
        columns_names = ['client_name', 'order', 'days_of_week']
        try:
            with open(path_to_file, newline="") as csvfile:
                reader = list(csv.DictReader(csvfile, columns_names))
        except NameError:
            raise FileNotFoundError(
                f"No such file or directory: '{path_to_file}'")
    else:
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    return reader


def most_wanted_order(orders):
    order_count = {}
    most_frequent = orders[0]

    for order in orders:
        if order not in order_count:
            order_count[order] = 1
        else:
            order_count[order] += 1
        if order_count[order] > order_count[most_frequent]:
            most_frequent = order
    return most_frequent


def count_orders_in_order(orders, order_to_match):
    count_order = 0
    for order in orders:
        if order_to_match == order:
            count_order += 1

    return count_order


def order_never_ordered_from_menu(joao_orders):
    menu = set(['hamburguer', 'pizza', 'coxinha', 'misto-quente'])
    orders = set(joao_orders)

    return menu.difference(orders)


def find_days_used(orders):
    days_used = []
    for orders in orders:
        if(orders['days_of_week'] not in days_used):
            days_used.append(orders['days_of_week'])
    return days_used


def days_with_no_order(days_used, days_with_order):
    days_of_week = set(days_used)
    days = set(days_with_order)

    return days_of_week.difference(days)


def write_file(filename, text):
    with open(filename, "a") as txtfile:
        txtfile.writelines(str(text) + "\n")
        txtfile.close()


def analyze_log(path_to_file):
    orders_history = read_file_to_dictionary(path_to_file)
    filename = 'data/mkt_campaign.txt'
    maria_orders = []
    arnaldo_orders = []
    joao_orders = []
    joao_weekdays = []

    for orders in orders_history:        
        if(orders['client_name'] == 'maria'):
            maria_orders.append(orders['order'])
        elif(orders['client_name'] == 'arnaldo'):
            arnaldo_orders.append(orders['order'])
        elif(orders['client_name'] == 'joao'):
            joao_orders.append(orders['order'])
            joao_weekdays.append(orders['days_of_week'])

    days = find_days_used(orders_history)
    write_file(filename, most_wanted_order(maria_orders))
    write_file(filename, count_orders_in_order(arnaldo_orders, 'hamburguer'))
    write_file(filename, order_never_ordered_from_menu(joao_orders))
    write_file(filename, days_with_no_order(days, joao_weekdays))
    # raise NotImplementedError
