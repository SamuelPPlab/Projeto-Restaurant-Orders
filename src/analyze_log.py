import csv


def all_orders_users(orders_list, customer):
    counter = {}
    orders_by_user = [
        order[1] for order in orders_list if customer == order[0]]
    for ordered_food in orders_by_user:
        if ordered_food not in counter:
            counter[ordered_food] = 1
        else:
            counter[ordered_food] += 1
    return counter


def most_ordered_by_user(orders_list, customer):
    all_orders_by_user = all_orders_users(orders_list, customer)
    most_commom = max(value for key, value in all_orders_by_user.items())
    dish = [
        key for key, value in all_orders_by_user.items()
        if all_orders_by_user[key] == most_commom][0]
    return dish


def times_ordered_food_by_user(orders_list, customer, dish):
    counter = 0
    for order in orders_list:
        if order[0] == customer and order[1] == dish:
            counter += 1
    return counter


def never_ordered_by_user(orders_list, customer):
    all_orders = set([order[1] for order in orders_list])
    customer_orders = set([
        order[1] for order in orders_list if order[0] == customer])
    return all_orders.difference(customer_orders)


def days_restaurant_not_visited(orders_list, customer):
    all_days = set([order[2] for order in orders_list])
    customer_days = set(
        [order[2] for order in orders_list if order[0] == customer])
    return all_days.difference(customer_days)


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        read_file = csv.reader(file, delimiter=',')
        orders_list = [row for row in read_file]

        most_ordered_by_maria = most_ordered_by_user(orders_list, 'maria')
        hamburguer_ordered_times_arnaldo = times_ordered_food_by_user(
            orders_list, 'arnaldo', 'hamburguer')
        never_ordered_by_joao = never_ordered_by_user(orders_list, 'joao')
        day_do_not_visited = days_restaurant_not_visited(
            orders_list, 'joao'
        )

    with open('./data/mkt_campaign.txt', mode="w") as file:
        file.write(f'{most_ordered_by_maria}\n')
        file.write(f'{hamburguer_ordered_times_arnaldo}\n')
        file.write(f'{never_ordered_by_joao}\n')
        file.write(f'{day_do_not_visited}\n')
