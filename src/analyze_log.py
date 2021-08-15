import csv


def orders_by_user(orders, user):
    foodCounter = {}
    foods = [row[1] for row in orders if row[0] == user]
    for food in foods:
        if food not in foodCounter:
            foodCounter[food] = 1
        else:
            foodCounter[food] += 1
    return foodCounter


def most_commom_order_by_user(orders, user):
    orders = orders_by_user(orders, user)
    return max(orders, key=orders.get)


def total_user_orders_by_food(orders, user, food):
    orders = orders_by_user(orders, user)
    return orders[food]


def not_requested_by_user(orders, user):
    requests = orders_by_user(orders, user)
    requested = set(list(requests))
    orders = set([row[1] for row in orders])
    return orders.difference(requested)


def days_not_ordered_by_user(orders, user):
    days_set = set([row[2] for row in orders])
    requested_days_array = [row[2] for row in orders if row[0] == user]
    requested_days_set = set(requested_days_array)
    return days_set.difference(requested_days_set)


def analyze_log(path_to_file):
    with open(path_to_file, mode="r") as file:
        orders = [row for row in csv.reader(file)]
        most_requested = most_commom_order_by_user(orders, 'maria')
        arnaldoRequests = total_user_orders_by_food(
            orders,
            'arnaldo',
            'hamburguer'
        )
        joaoNotRequested = not_requested_by_user(orders, 'joao')
        joaoNeverBought = days_not_ordered_by_user(orders, 'joao')

    with open('data/mkt_campaign.txt', mode='w+') as file:
        file.write(f'{most_requested}\n')
        file.write(f'{str(arnaldoRequests)}\n')
        file.write(f'{str(joaoNotRequested)}\n')
        file.write(f'{str(joaoNeverBought)}\n')
