import csv
import operator


def get_orders(path):
    order_tuples = []

    # source: https://www.programiz.com/python-programming/reading-csv-files
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for order in reader:
            order_tuples.append(tuple(order))

    return order_tuples


def analyze_maria_orders(orders):
    maria_meals = {}

    for order in orders:
        if order[0] == 'maria':
            if order[1] in maria_meals:
                maria_meals[order[1]] += 1
            else:
                maria_meals[order[1]] = 1

    # source:
    # https://stackoverflow.com/questions/
    # 268272/getting-key-with-maximum-value-in-dictionary
    most_common = max(maria_meals.items(), key=operator.itemgetter(1))[0]
    return most_common


def analyze_arnaldo_orders(orders):
    arnaldo_burguers = 0

    for order in orders:
        if order[0] == 'arnaldo' and order[1] == 'hamburguer':
            arnaldo_burguers += 1

    return arnaldo_burguers


def filter_joao_orders(meal_options, joao_orders):
    updated_meal_options = set()

    for meal in meal_options:
        if meal not in joao_orders:
            updated_meal_options.add(meal)

    return updated_meal_options


def analyze_joao_never_ordered(orders):
    meal_options = []
    joao_orders = []

    for order in orders:
        if order[1] not in meal_options:
            meal_options.append(order[1])

        if order[0] == 'joao':
            joao_orders.append(order[1])

    never_ordered = filter_joao_orders(meal_options, joao_orders)

    return never_ordered


def filter_customer_days(days, days_customer):
    updated_days = set()

    for day in days:
        if day not in days_customer:
            updated_days.add(day)

    return updated_days


def analyze_customer_days(orders):
    days = []
    days_customer = []

    for order in orders:
        if order[2] not in days:
            days.append(order[2])

        if order[0] == 'joao':
            days_customer.append(order[2])

    never_went = filter_customer_days(days, days_customer)

    return never_went


def analyze_log(path):
    orders = get_orders(path)

    maria_most_ordered = analyze_maria_orders(orders)
    arnaldo_burguers = analyze_arnaldo_orders(orders)
    joao_never_ordered = analyze_joao_never_ordered(orders)
    customer_never_went = analyze_customer_days(orders)

    result = (
        maria_most_ordered,
        arnaldo_burguers,
        joao_never_ordered,
        customer_never_went
    )

    with open('data/mkt_campaign.txt', 'w') as file:
        index = 0

        for line in result:
            index += 1
            formated_line = str(line)

            if index < len(result):
                file.write(formated_line + '\n')
            else:
                file.write(formated_line)
