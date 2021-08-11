import csv


def create_txt(name, content):
    try:
        file = open("data/{}".format(name), 'r+')
        file.writelines(content)
    except FileNotFoundError:
        file = open("data/{}".format(name), 'w+')
        file.writelines(content)
    file.close()


def day_of_week(list_orders, costumer):
    days_of_joao = []
    all_days = []
    for order in list_orders:
        if order[0] == costumer:
            days_of_joao.append(order[2])
        all_days.append(order[2])

    result = {
        item for item in sorted(set(all_days))
        if item not in days_of_joao
    }
    return result


def max_order(order_list, costumer):
    orders_costumer = []
    all_products = list(product for product in order_list)
    for item in all_products:
        if item[0] == costumer:
            orders_costumer.append(item[1])

    return max(set(orders_costumer), key=orders_costumer.count)


def never_order(list_order, costumer):
    order = []
    all_itens = list(option[1] for option in list_order)

    for item in list_order:
        if item[0] == costumer:
            order.append(item[1])
    return {
        item for item in sorted(set(all_itens)) if item not in order
    }


def analyze_log(path_to_file):
    if ".csv" not in path_to_file:
        raise FileNotFoundError(
            "No such file or directory: " "'{}'"
            .format(path_to_file))
    else:
        with open(path_to_file) as csvfile:
            count = 0
            doc_reader = csv.reader(csvfile)
            data_csv = list((item for item in doc_reader))
            for request in data_csv:
                if request[0] == 'arnaldo':
                    if request[1] == 'hamburguer':
                        count += 1

    create_txt(
        'mkt_campaign.txt',
        f"{max_order(data_csv, 'maria')}\n{count}" +
        f"\n{never_order(data_csv, 'joao')}" +
        f"\n{day_of_week(data_csv,'joao')}"
    )
