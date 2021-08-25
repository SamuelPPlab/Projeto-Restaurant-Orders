import csv


def count_meal(lines, person, meals):
    orders = {}
    for meal in meals:
        orders[meal] = 0
    for line in lines:
        if line['name'] == person:
            orders[line['food']] += 1

    return orders


def get_keys_with_value_zero(meals):
    never_ordered = list()
    for o in meals:
        if meals[o] == 0:
            never_ordered.append(o)
    return never_ordered


def count_chosen_meal(lines, person, meal):
    counter = 0
    for line in lines:
        if line['name'] == person:
            if line['food'] == meal:
                counter += 1

    return counter


def count_days(lines, person, days):
    orders = {}
    for day in days:
        orders[day] = 0
    for line in lines:
        if line['name'] == person:
            orders[line['day']] += 1
    return orders


def organize_orders(file):
    file_read = csv.DictReader(file, fieldnames=['name', 'food', 'day'])
    list_dict = list(file_read)
    set_names = set()
    set_food = set()
    set_day = set()
    for n in list_dict:
        set_names.add(n['name'])
        set_food.add(n['food'])
        set_day.add(n['day'])

    maria_count_meal = count_meal(list_dict, 'maria', set_food)
    maria_favorite_meal = max(maria_count_meal, key=maria_count_meal.get)
    arnaldo_hamburger_orders_nbr = count_chosen_meal(
        list_dict, 'arnaldo', 'hamburguer'
    )
    joao_orders = count_meal(list_dict, 'joao', set_food)
    joao_never_ordered = get_keys_with_value_zero(joao_orders)
    joao_weekdays_count = count_days(list_dict, 'joao', set_day)
    joao_weekdays_without_orders = get_keys_with_value_zero(
        joao_weekdays_count
    )

    response = f"{maria_favorite_meal}\n{arnaldo_hamburger_orders_nbr}"\
        f"\n{set(joao_never_ordered)}\n{set(joao_weekdays_without_orders)}"

    txt_file = open('data/mkt_campaign.txt', 'w')
    txt_file.writelines(response)
    txt_file.close()


def analyze_log(path_to_file):
    with open(path_to_file) as csvfile:
        return(organize_orders(csvfile))


analyze_log('data/orders_1.csv')
