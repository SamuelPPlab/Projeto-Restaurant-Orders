import csv


def analyze_log(path_to_file):
    if (not path_to_file.endswith('csv')):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    log_list = generate_array_with_orders(path_to_file)
    write_log_response(log_list)


def generate_array_with_orders(path_to_file):
    try:
        loglist = []
        reader = csv.DictReader(open(path_to_file, 'r'))
        for row in reader:
            loglist.append(list(row.values()))
        return loglist
    except():
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")


def write_log_response(list_orders):
    log = []
    log.append(generate_most_frequent_maria_order(list_orders))
    log.append(generate_how_much_hamburguers_arnaldo_ordered(list_orders))
    log.append(generate_foods_that_joao_never_ordered(list_orders))
    log.append(generate_joao_absence_days(list_orders))
    with open("data/mkt_campaign.txt", "w") as outfile:
        outfile.write("\n".join(log))


def generate_most_frequent_maria_order(list_orders):
    maria_orders = filter(lambda x: x[0] == 'maria', list_orders)
    maria_orders = list(map(lambda x: x[1], maria_orders))
    return max(set(maria_orders), key=maria_orders.count)


def generate_how_much_hamburguers_arnaldo_ordered(list_orders):
    arnaldo_ordered = list(filter(lambda x: x[0] == 'arnaldo' and
                           x[1] == 'hamburguer', list_orders))
    return str(len(arnaldo_ordered))


def generate_foods_that_joao_never_ordered(list_orders):
    joao_all_orders = filter(lambda x: x[0] == 'joao', list_orders)
    joao_all_orders = set(map(lambda x: x[1], joao_all_orders))
    all_foods_orders = generate_all_foods_ordered(list_orders)
    return str(joao_all_orders.symmetric_difference(all_foods_orders))


def generate_all_foods_ordered(list_orders):
    return set(map(lambda x: x[1], list_orders))


def generate_joao_absence_days(list_orders):
    days_of_the_week = generate_all_days_of_the_week(list_orders)
    joao_days = generate_joao_days(list_orders)
    return str(days_of_the_week.symmetric_difference(joao_days))


def generate_all_days_of_the_week(list_orders):
    return set(map(lambda x: x[2], list_orders))


def generate_joao_days(list_orders):
    joao_all_orders = filter(lambda x: x[0] == 'joao', list_orders)
    return set(map(lambda x: x[2], joao_all_orders))
