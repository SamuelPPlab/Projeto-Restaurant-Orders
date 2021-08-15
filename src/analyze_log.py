import csv


def get_file_csv(file_path):
    with open(file_path) as fd:
        list_restaurant = list(csv.reader(fd))
    return list_restaurant


def filter_list_client_by_name(list_clients, name):
    new_list = []
    for item in list_clients:
        if name in item:
            new_list.append(item)
    return new_list


def filter_foods_not_repeated_in_list(array):
    new_list = []
    for item in array:
        if item[1] not in new_list:
            new_list.append(item[1])
    return new_list


def filter_days_of_the_week_not_repeated_in_list(array):
    new_list = []
    for item in array:
        if item[2] not in new_list:
            new_list.append(item[2])
    return new_list


def get_food_max_repeat_in_list(list_food_by_name, list_food):
    max_value = 0
    most_food = ""
    count = 0

    for food in list_food:
        for item in list_food_by_name:
            if food in item:
                count += 1
        if count > max_value:
            most_food = food
            max_value = count
        count = 0
    return most_food


def get_most_requested_dish_by_name(file, name):
    list_food_by_name = filter_list_client_by_name(file, name)
    list_food = filter_foods_not_repeated_in_list(list_food_by_name)
    return get_food_max_repeat_in_list(list_food_by_name, list_food)


def save_text(text):
    FILE_TXT = "data/mkt_campaign.txt"
    with open(FILE_TXT, "a") as fd:
        fd.write(text + "\n")


def transform_list_to_string(array):
    frase = ""
    for i in range(len(array)):
        if i == len(array) - 1:
            frase += f"'{array[i]}'"
            break
        frase += f"'{array[i]}',"

    frase = "{" + frase + "}"
    return frase


def count_works_in_linst(array, work):
    count = 0
    for item in array:
        if work in item:
            count += 1
    return count


def get_how_many_times_did_anyware_ask_food_by_name_food(
    file, name_client, name_food
):
    list_food_by_name_client = filter_list_client_by_name(file, name_client)
    count_work = count_works_in_linst(list_food_by_name_client, name_food)
    return count_work


def what_dishes_did_client_never_order(file, name_client):
    list_foods = []

    foods = filter_foods_not_repeated_in_list(file)
    list_food_joao = filter_list_client_by_name(file, name_client)
    foods_joao = filter_foods_not_repeated_in_list(list_food_joao)

    for food in foods:
        if food not in foods_joao:
            list_foods.append(food)

    return transform_list_to_string(list_foods)


def what_days_client_never_went_to_the_cafeteria(file, name_client):
    list_days = []

    days_of_day_week = filter_days_of_the_week_not_repeated_in_list(file)
    list_joao = filter_list_client_by_name(file, name_client)
    days_of_day_week_of_joao = filter_days_of_the_week_not_repeated_in_list(
        list_joao
    )

    for day in days_of_day_week:
        if day not in days_of_day_week_of_joao:
            list_days.append(day)
    list_days.reverse()

    return transform_list_to_string(list_days)


def analyze_log(path_to_file):

    file = get_file_csv(path_to_file)

    food = get_most_requested_dish_by_name(file, "maria")
    save_text(food)

    count = get_how_many_times_did_anyware_ask_food_by_name_food(
        file, "arnaldo", "hamburguer"
    )
    save_text(str(count))

    frase = what_dishes_did_client_never_order(file, "joao")
    save_text(frase)

    days = what_days_client_never_went_to_the_cafeteria(file, "joao")
    save_text(days)
