import csv


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

    # order[1] = plate ordered
    # order[0] = client that make order
    for order in orders:
        if order[0] == name and order[1] == plate:
            client_order.add(order[1])
    return len(client_order)


def plates_never_ordered(name, orders):
    order_client = set()
    all_orders = set()

    # order[1] = plate ordered
    # order[0] = client that make order
    for order in orders:
        all_orders.add(order[1])
    for order in orders:
        if order[0] == name:
            order_client.add(order[1])
    return all_orders.difference(order_client)


def days_without_orders(name, orders):
    days_with_orders = set()
    all_days = set()

    # order[2] = day of order
    # order[0] = client that make order
    for order in orders:
        all_days.add(order[2])
    for order in orders:
        if order[0] == name:
            days_with_orders.add(order[2])
    return all_days.difference(days_with_orders)


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
