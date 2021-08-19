import csv


def find_and_format_data(path):
    file = open(path, 'r')
    orders_reader = csv.reader(file)
    orders = {}
    foods = set()
    days_of_the_week = set()
    for name, food, day in orders_reader:
        foods.add(food)
        days_of_the_week.add(day)
        if name not in orders:
            orders[name] = [{"food": food, "day_of_the_week": day}]
        else:
            orders[name].append({"food": food, "day_of_the_week": day})
    return orders, foods, days_of_the_week


def maria_most_ordered(orders):
    count = {}
    most_frequent = orders["maria"][0]["food"]
    for order in orders["maria"]:
        if order["food"] not in count:
            count[order["food"]] = 1
        else:
            count[order["food"]] += 1
        if count[order["food"]] > count[most_frequent]:
            most_frequent = order["food"]
    return most_frequent


def arnaldo_times_ordered(orders):
    count = 0
    for order in orders["arnaldo"]:
        if order["food"] == "hamburguer":
            count += 1
    return count


def joao_never(orders, all_query_items, query):
    seen_before = set()
    all = set(all_query_items)
    print(set(query))
    for order in orders["joao"]:
        seen_before.add(order[query])
    print(seen_before)
    return all.difference(seen_before)


def analyze_log(path_to_file):
    orders, food, day = find_and_format_data(path_to_file)
    maria_favorite_order = maria_most_ordered(orders)
    arnaldo_frequency_order = arnaldo_times_ordered(orders)
    joao_never_product = joao_never(orders, food, "food")
    joao_never_day = joao_never(orders, day, "day_of_the_week")
    file = open("data/mkt_campaign.txt", 'w')
    file.write(f"{maria_favorite_order}\n")
    file.write(f"{arnaldo_frequency_order}\n")
    file.write(f"{joao_never_product}\n")
    file.write(f"{joao_never_day}\n")
    file.close()
