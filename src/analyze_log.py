import collections
import csv


def get_all_orders(file_path):
    with open(file_path, 'r') as file:
        # file_to_dict = csv.DictReader(file)  # method for give keys
        # for row in file_to_dict:
        #     row['k1_customer'], row['k2_ordered_dish'], row['k3_week_day']
        keys = ['k1_customer', 'k2_ordered_dish', 'k3_week_day']
        file_to_dict = csv.DictReader(file, fieldnames=keys)
        all_orders = []
        [all_orders.append(requests) for requests in file_to_dict]
        # print('ALL ORDERS', all_orders)
    return all_orders


def most_ordered_dishes(customer, all_orders):
    ordered_dishs = [
        order['k2_ordered_dish']
        for order in all_orders
        if order['k1_customer'] == customer
    ]
    most_order_dish = collections.Counter(ordered_dishs).most_common(1)[0][0]
    return most_order_dish


def dish_quantity(customer, dish, all_orders):
    all_dishs_customer = [
        order['k2_ordered_dish']
        for order in all_orders
        if order['k1_customer'] == customer
    ]
    count_dish = collections.Counter(all_dishs_customer).get(dish)
    return count_dish


def never_ordered(customer, all_orders):
    dishs_types = {
        order['k2_ordered_dish']
        for order in all_orders
    }
    ordered_dish_customer = {
        order['k2_ordered_dish']
        for order in all_orders
        if order['k1_customer'] == customer
    }

    dish_never_ordered = dishs_types ^ ordered_dish_customer
    return dish_never_ordered


def days_never_visited(customer, all_orders):
    get_all_days = {
        week_day['k3_week_day']
        for week_day in all_orders
    }
    days_in = {
        week_day['k3_week_day']
        for week_day in all_orders
        if week_day['k1_customer'] == customer
    }
    days_out = get_all_days ^ days_in
    return days_out


def analyze_log(file_path):
    if file_path.endswith('.csv'):
        txt_file = 'data/mkt_campaign.txt'
        all_orders = get_all_orders(file_path)
        txt = [
            f"{most_ordered_dishes('maria', all_orders)}\n",
            f"{dish_quantity('arnaldo','hamburguer',all_orders)}\n",
            f"{never_ordered('joao', all_orders)}\n",
            f"{days_never_visited('joao', all_orders)}",
        ]
        with open(txt_file, 'w') as arquivo:
            arquivo.writelines(txt)

        # most_ordered_dishe = most_ordered_dishes('maria', all_orders)
        # count_d_by_c = dish_quantity('arnaldo','hamburguer',all_orders)
        # get_nonexistent_orders = never_ordered('joao', all_orders)
        # days_not_in = days_never_visited('joao', all_orders)
        # txt = [
        #     f'{most_ordered_dishe}\n',
        #     f'{count_d_by_c}\n',
        #     f'{get_nonexistent_orders}\n',
        #     f'{days_not_in}',
        # ]
        # with open(txt_file, 'w') as arquivo:
        #     arquivo.writelines(txt)

        # txt = []
        # txt.append(most_ordered_dishes('maria', all_orders))
        # txt.append(dish_quantity('arnaldo', 'hamburguer', all_orders))
        # txt.append(never_ordered('joao', all_orders))
        # txt.append(days_never_visited('joao', all_orders))
        # with open(txt_file, 'w') as file:  # 05
        #     for element in txt:
        #         file.write(str(element) + "\n")
    else:
        raise FileNotFoundError(
            f"No such file or directory: '{file_path}'"
        )


if __name__ == '__main__':
    analyze_log('data/orders_1.csv')

# python3 -m pytest tests/test_analyze_log.py
# $ source .venv/bin/activate

# referencias
# Tive ajuda de ZecaCosta T6,T7
# 01 - https://docs.python.org/3/library/csv.html
# 02 - https://docs.python.org/3/library/collections.html
# 03 - https://www.codegrepper.com/code-examples/python/python+collections...
# 04 - https://stackoverflow.com/questions/50871370/python-sets-difference...
# 04 - https://www.programiz.com/python-programming/methods/set/symmetric_...
# 05 - https://stackoverflow.com/questions/37289951/how-to-write-to-a-csv-...
# 06 - https://www.pythonforbeginners.com/files/reading-and-writing-files-...
# https://www.geeksforgeeks.org/defaultdict-in-python/
