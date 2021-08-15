import csv


def __add_foods_in_orders_resume(orders_resume, orders):
    foods = [order[1] for order in orders]
    for order in orders:
        name, food, day = order
        for food in foods:
            if food not in orders_resume[name]['foods']:
                orders_resume[name]['foods'][food] = 0
    return orders_resume


def __orders_resume(orders):
    orders_resume = {}

    for order in orders:
        name, food, day = order
        if name not in orders_resume:
            orders_resume[name] = {'foods': {}, 'days': []}
        if food not in orders_resume[name]['foods']:
            orders_resume[name]['foods'][food] = 1
        else:
            orders_resume[name]['foods'][food] += 1
        if day not in orders_resume[name]['days']:
            orders_resume[name]['days'].append(day)
    
    orders_resume = __add_foods_in_orders_resume(orders_resume, orders)

    return orders_resume


def more_requested_by_client(orders, client_name):
    orders_resume = __orders_resume(orders)[client_name]['foods']
    orders_resume = dict(
        sorted(orders_resume.items(), key=lambda x: x[1], reverse=True)
    )
    key_orders = [key for key, value in orders_resume.items()]
    return key_orders[0]


def count_eat_by_client(orders, eat_name, client_name):
    orders_by_client_and_eat = [
        client[1] for client in orders
        if client[0] == client_name and client[1] == eat_name
    ]
    return len(orders_by_client_and_eat)


def never_order_by_client(orders, client_name):
    orders_resume = __orders_resume(orders)[client_name]['foods']
    key_orders = [
        key for key, value in orders_resume.items() if value == 0
    ]
    return set(key_orders)


def days_not_present_client(orders, client_name):
    days = ['segunda-feira', 'terça-feira', 'sabado']
    orders_resume_days = __orders_resume(orders)[client_name]['days']
    never_days = [day for day in days if day not in orders_resume_days]
    return set(never_days)


def analyze_log(path_to_file):
    with open(path_to_file, 'r') as file:
        get_clients = csv.reader(file, delimiter=",")
        clients = [item for item in get_clients]

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(f'{more_requested_by_client(clients, "maria")}\n')
        file.write(f'{count_eat_by_client(clients, "hamburguer", "arnaldo")}\n')
        file.write(f'{never_order_by_client(clients, "joao")}\n')
        file.write(f'{days_not_present_client(clients, "joao")}')
