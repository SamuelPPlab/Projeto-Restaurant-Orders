import csv
from collections import Counter


def most_requested_dish(orders, person):
    person_orders = list(map(lambda order: order[1], filter(
        lambda name: name[0] == person, orders)))
    return (Counter(person_orders).most_common(1))[0][0]


def how_many_times_was_requested(orders, person, dish):
    person_orders = list(filter(
        lambda name: name[0] == person and name[1] == dish, orders))
    print(len(person_orders))
    return len(person_orders)


def never_requested_dishes(orders, person):
    dishes = set([order[1] for order in orders])
    person_orders = set(list(map(lambda order: order[1], filter(
        lambda name: name[0] == person, orders))))
    return dishes.difference(person_orders)


def never_attended_days(orders, person):
    days = set([order[2] for order in orders])
    person_orders = set(
            [order[2] for order in orders if order[0] == person]
        )
    return (days.difference(person_orders)).sort()


def analyze_log(path_to_file):
    result_list = list()

    with open(path_to_file, mode="r") as file:
        orders = [row for row in csv.reader(file)]

        requested = most_requested_dish(orders, 'maria')
        result_list.append(f"{requested}\n")

        times = how_many_times_was_requested(orders, 'arnaldo', 'hamburguer')
        result_list.append(f"{times}\n")

        never_requested = never_requested_dishes(orders, 'joao')
        result_list.append(f"{never_requested}\n")

        never_attended = never_attended_days(orders, 'joao')
        result_list.append(f"{never_attended}\n")

    with open("./data/mkt_campaign.txt", mode="w") as file:
        file.writelines(result_list)




""" x = [['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'hamburguer', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira']]
print(never_attended_days(x, 'joao')) """