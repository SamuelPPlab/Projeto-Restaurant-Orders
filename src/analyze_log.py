import csv


# def importDataCsv(file_name):
#     if file_name.split('.')[1] != 'csv':
#         raise ValueError('Arquivo inválido')

#     with open(file_name) as file:
#         data = csv.reader(file, delimiter=",")
#         report_list = list(data)
#     return report_list


def favorite_plate(name, orders):
    plates_count = dict()
    max_order_plate = 0
    favorite_plate = ""
    for order in orders:

        # checking if client ordered is equal to name
        if order[0] == name:

            # checkint if plate are already on plates_count dict
            if order[1] in plates_count:
                plates_count[order[1]] += 1
            else:
                plates_count[order[1]] = 1

            # checking if actual plate on plates count is the most requested
            if plates_count[order[1]] > max_order_plate:
                max_order_plate = plates_count[order[1]]
                favorite_plate = order[1]
    return favorite_plate


def plates_repeated(name, plate, orders):
    client_order = set()
    for order in orders:
        if order[0] == name and order[1] == plate:
            client_order.add(order[1])
    return len(client_order)


def plates_never_ordered(name, orders):
    order_client = set()
    all_orders = set()
    for order in orders:
        all_orders.add(order[1])
    for client in orders:
        if client[0] == name:
            order_client.add(client[1])
    return all_orders.difference(order_client)


def days_without_orders(name, days):
    days_without_orders = set()
    all_days = set()
    for day in days:
        all_days.add(day[2])
    for day in days:
        if day[0] == name:
            days_without_orders.add(day[2])
    return all_days.difference(days_without_orders)


def analyze_log(path_to_file):
    # orders = importDataCsv(path_to_file)
    if path_to_file.split('.')[1] != 'csv':
        path_to_file_txt = path_to_file.replace("'", "") + "'"
        eror_msg = "No such file or directory: '" + path_to_file_txt
        raise FileNotFoundError(eror_msg)

    with open(path_to_file) as file:
        data = csv.reader(file, delimiter=",")
        orders = list(data)

    with open("data/mkt_campaign.txt", "w") as analyze_file:
        # first requirement
        analyze_file.write(f"{favorite_plate('maria', orders)}\n")
        # second requirement
        analyze_file.write(
            f"{plates_repeated('arnaldo','hamburguer', orders)}\n"
        )
        # # third requirement
        analyze_file.write(
            f"{plates_never_ordered('joao', orders)}\n"
        )
        # # fourth requirement
        analyze_file.write(f"{days_without_orders('joao', orders)}\n")
