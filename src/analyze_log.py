import csv


def main(read_orders):
    orders = {}
    products = set()
    days = set()

    for name, item, day in read_orders:
        products.add(item)
        days.add(day)
        if name not in orders:
            orders[name] = [{"product": item, "days": day}]
        else:
            orders[name].append({"product": item, "days": day})

    return orders, products, days


def read_csv(path):
    with open(path, "r") as file:
        read_orders = csv.reader(file, delimiter=",", quotechar='"')
        orders = main(read_orders)
    return orders


def more_requests(orders, name):
    count_object = {}
    most_frequent_product = orders[name][0]["product"]
    for order in orders[name]:
        if (
            count_object[order["product"]]
            > count_object[most_frequent_product]
        ):
            most_frequent_product = order["product"]
        elif order["product"] not in count_object:
            count_object[order["product"]] = 1
        else:
            count_object[order["product"]] += 1

    return most_frequent_product


def times_requests(orders, name, item):
    count = 0
    for order in orders[name]:
        if order["product"] == item:
            count += 1
    return count


def never_asked(orders, name, list_of, term):
    products = set()
    set_list = set(list_of)
    for order in orders[name]:
        products.add(order[term])

    return set_list.difference(products)


def analyze_log(path_to_file):
    orders, products, days = read_csv(path_to_file)
    maria_requests = more_requests(orders, "maria")
    arnaldo_requests = times_requests(orders, "arnaldo", "hamburguer")
    joao_never_request = never_asked(orders, "joao", products, "product")
    joao_never_visited = never_asked(orders, "joao", days, "days")

    file = open("data/mkt_campaign.txt", "w")
    file.write(f"{maria_requests}\n")
    file.write(f"{arnaldo_requests}\n")
    file.write(f"{joao_never_request}\n")
    file.write(f"{joao_never_visited}")
