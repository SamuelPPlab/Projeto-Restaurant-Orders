import csv
from collections import Counter


def unordered_request(list_order, food_list):
    menu = order_set(list_order)
    food_set = set()
    for food in food_list:
        food_set.add(food[0])
    return menu.difference(food_set)


def count_food(order_list):
    food_list = []
    for order in order_list:
        food_list.append(order['order'])
    return Counter(food_list).most_common()


def count_hamburguer(order_list):
    food_list = []
    for order in order_list:
        food_list.append(order['order'])
    return Counter(food_list)['hamburguer']


def order_by_client(client, list_dict):
    def filter_client(dict):
        if dict["name"] == client:
            return True
        return False
    return list(filter(filter_client, list_dict))


def import_data_csv(path):
    with open(path, mode="r") as file:
        fields = ["name", "order", "day"]
        return list(csv.DictReader(file, fields))


def order_set(list_order):
    foods_menu = set()
    for order in list_order:
        foods_menu.add(order['order'])
    return foods_menu


def didnt_go(list_order, client_order):
    set_day = set()
    for order in list_order:
        set_day.add(order['day'])
    set_days_food = set()
    for order in client_order:
        set_days_food.add(order['day'])
    return set_day.difference(set_days_food)


def write_answer(list_answer):
    with open("./data/mkt_campaign.txt", mode="w") as file:
        for item in list_answer:
            file.write(f"{item}\n")


def maria_food(list_orders):
    filter_list_maria = order_by_client("maria", list_orders)
    return count_food(filter_list_maria)[0][0]


def hamburguer_arnaldo(list_orders):
    filter_list_arnaldo = order_by_client("arnaldo", list_orders)
    return count_hamburguer(filter_list_arnaldo)


def joao_unordered(list_orders):
    filter_list_joao = order_by_client("joao", list_orders)
    joao_food = count_food(filter_list_joao)
    return unordered_request(list_orders, joao_food)


def joao_didnt_go(list_orders):
    filter_list_joao = order_by_client("joao", list_orders)
    return didnt_go(list_orders, filter_list_joao)


def analyze_log(path_to_file):
    list_answer = []
    list_orders = import_data_csv(path_to_file)
    maria_most_food = maria_food(list_orders)
    hamburguer_arnaldo_asked = hamburguer_arnaldo(list_orders)
    joao_unordered_foods = joao_unordered(list_orders)
    joao_didnt_go_days = joao_didnt_go(list_orders)
    list_answer.append(maria_most_food)
    list_answer.append(hamburguer_arnaldo_asked)
    list_answer.append(joao_unordered_foods)
    list_answer.append(joao_didnt_go_days)
    write_answer(list_answer)
