import csv


def orders_by_user(orders, user):
    food_counter = {}
    requested_food_array = [row[1] for row in orders if row[0] == user]
    for requested_food in requested_food_array:
        if requested_food not in food_counter:
            food_counter[requested_food] = 1
        else:
            food_counter[requested_food] += 1

    return food_counter


def most_commom_order_by_user(orders, user):
    requests = orders_by_user(orders, user)
    return max(requests, key=requests.get)


def total_user_orders_by_food(orders, user, food):
    requests = orders_by_user(orders, user)
    return requests[food]


def not_requested_by_user(orders, user):
    requests = orders_by_user(orders, user)
    requested_set = set(list(requests))
    orders_set = set([row[1] for row in orders])
    return orders_set.difference(requested_set)


def days_not_ordered_by_user(orders, user):
    days_set = set([row[2] for row in orders])
    requested_days_array = [row[2] for row in orders if row[0] == user]
    requested_days_set = set(requested_days_array)
    return days_set.difference(requested_days_set)


def analyze_log(path_to_file):
    with open(path_to_file, mode="r") as file:
        orders = [row for row in csv.reader(file)]
        most_requested = most_commom_order_by_user(orders, 'maria')
        arnaldo__hamburguer_requests = total_user_orders_by_food(
            orders,
            'arnaldo',
            'hamburguer'
        )
        joao_never_requested = not_requested_by_user(orders, 'joao')
        joao_never_went = days_not_ordered_by_user(orders, 'joao')

    with open('data/mkt_campaign.txt', mode='w+') as file:
        file.write(f'{most_requested}\n')
        file.write(f'{str(arnaldo__hamburguer_requests)}\n')
        file.write(f'{str(joao_never_requested)}\n')
        file.write(f'{str(joao_never_went)}\n')
