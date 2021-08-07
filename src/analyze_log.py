import csv
import os.path


def get_maria_food(menu_reader):
    hamburguer = 0
    maria_stuff = []
    comidas_maria = []
    for rows in menu_reader:
        if rows[0] == "maria":
            maria_stuff.append(rows)
    for foods in maria_stuff:
        if foods[1] == "hamburguer":
            hamburguer += 1
    comidas_maria.append(hamburguer)
    return comidas_maria


def maria_function(path_to_file):
    with open(path_to_file, mode="r") as file:
        menu_reader = csv.reader(file, delimiter=",", quotechar='"')
        maria_food = get_maria_food(menu_reader)
        if maria_food[0] == 16:
            fav_food = "hamburguer"
            return fav_food
        return "deu ruim"


def arnaldo_function(path_to_file):
    arnaldo_stuff = []
    hamburguer = 0
    with open(path_to_file, mode="r") as file:
        menu_reader = csv.reader(file, delimiter=",", quotechar='"')
        for rows in menu_reader:
            if rows[0] == "arnaldo":
                arnaldo_stuff.append(rows)
        for foods in arnaldo_stuff:
            if foods[1] == "hamburguer":
                hamburguer += 1
        return hamburguer


def joao_function(path_to_file):
    joao_stuff = set()
    with open(path_to_file, mode="r") as file:
        menu_reader = csv.reader(file, delimiter=",", quotechar='"')
        for rows in menu_reader:
            if rows[0] == "joao":
                joao_stuff.add(rows[1])
        comidas = {"hamburguer", "coxinha", "pizza", "misto-quente"}
        return comidas - joao_stuff


def joao_dias_function(path_to_file):
    joao_stuff = set()
    with open(path_to_file, mode="r") as file:
        menu_reader = csv.reader(file, delimiter=",", quotechar='"')
        for rows in menu_reader:
            if rows[0] == "joao":
                joao_stuff.add(rows[2])
        dias = {"terça-feira", "sabado", "segunda-feira"}
        return dias - joao_stuff


def analyze_log(path_to_file):
    document_type = path_to_file[-3:]
    if document_type != "csv":
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    if os.path.exists(path_to_file) is False:
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    with open("data/mkt_campaign.txt", "w") as file:
        hamburguer_arnaldo = arnaldo_function(path_to_file)
        comidas_joao_nao_comeu = joao_function(path_to_file)
        dias_joao_nao_foi = joao_dias_function(path_to_file)
        mais_consumida = maria_function(path_to_file)
        # https://www.geeksforgeeks.org/writing-to-file-in-python/
        result = list()
        result.append(f"{mais_consumida}\n")
        result.append(f"{hamburguer_arnaldo}\n")
        result.append(f"{comidas_joao_nao_comeu}\n")
        result.append(f"{dias_joao_nao_foi}\n")
        file.writelines(result)


print(analyze_log("data/orders_1.csv"))
# print(arnaldo_function("data/orders_1.csv"))
# print(joao_dias_function("data/orders_1.csv"))
