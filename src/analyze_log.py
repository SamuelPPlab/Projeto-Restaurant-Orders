import csv

people = set()
foods = set()
days = set()

person_foods = dict()
person_days = dict()


def populate_person_foods(person, food):
    if person not in person_foods:
        person_foods[person] = {}

    if food not in person_foods[person]:
        person_foods[person][food] = 1
    else:
        person_foods[person][food] += 1


def populate_person_days(person, day):
    if person not in person_days:
        person_days[person] = {}

    if day not in person_days[person]:
        person_days[person][day] = 1
    else:
        person_days[person][day] += 1


def populate_lists(person, food, day):
    people.add(person)
    foods.add(food)
    days.add(day)


def read_data(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")

        for line in reader:
            person, food, day = line

            populate_lists(person, food, day)
            populate_person_foods(person, food)
            populate_person_days(person, day)


def save_data(data):
    with open("data/mkt_campaign.txt", mode="w") as file:
        last_line = len(data) - 1

        for index, line in enumerate(data):
            file.write(f"{str(line)}")

            if index != (last_line):
                file.write("\n")


def get_most_ordered_food_by_person(person_name):
    bigger_quantity = 0
    most_ordered = ""

    for order, quantity in person_foods[person_name].items():
        if quantity > bigger_quantity:
            bigger_quantity = quantity
            most_ordered = order

    return most_ordered


def get_food_count_by_person(person_name, food_name):
    return person_foods[person_name][food_name]


def get_never_ordered_foods_by_person(person_name):
    person_orders = set(person_foods[person_name])

    return foods.difference(person_orders)


def get_not_frequented_days_by_person(person_name):
    person_frequency = set(person_days[person_name])

    return days.difference(person_frequency)


def analyze_log(path_to_file):
    read_data(path_to_file)

    food_most_ordered_by_maria = get_most_ordered_food_by_person("maria")
    arnaldo_burger_count = get_food_count_by_person("arnaldo", "hamburguer")
    joao_never_ordered_foods = get_never_ordered_foods_by_person("joao")
    joao_never_visited_days = get_not_frequented_days_by_person("joao")

    save_data(
        (
            food_most_ordered_by_maria,
            arnaldo_burger_count,
            joao_never_ordered_foods,
            joao_never_visited_days,
        )
    )
