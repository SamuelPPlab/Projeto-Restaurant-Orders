from src.csv_importer import CsvImporter
from src.client import client


def data_organize(data):
    days = {
        # "domingo": 0,
        "segunda-feira": 0,
        "terça-feira": 0,
        # "quarta-feira": 0,
        # "quinta-feira": 0,
        # "sexta-feira": 0,
        "sabado": 0,
    }
    data_client = {}

    for item in data:
        name = item[0]
        food = item[1]
        day = item[2]

        if name not in data_client:
            data_client[name] = {"days": days.copy(), "foods": {}}
        data_client[name]["days"][day] += 1

        if food in data_client[name]["foods"]:
            data_client[name]["foods"][food] += 1
        else:
            data_client[name]["foods"].update({food: 1})

    return data_client


def most_popular_food(foods):
    return max(foods, key=foods.get)


def most_popular_food2(client_name, clients_dict):
    foods = clients_dict[client_name].foods
    return max(foods, key=foods.get)


def generate_menu(data):
    menu = set()
    for value in data.values():
        for food in value["foods"].keys():
            menu.add(food)
    return menu


def analyze_log(path_to_file):
    data = data_organize(CsvImporter.import_data(path_to_file))
    menu = generate_menu(data)

    clients = dict()
    for key, value in data.items():
        person = client(key, value["foods"], value["days"])
        clients[key] = person

    joao_not_order = menu.difference(clients["joao"].foods.keys())

    joao_at_home = set()
    joao_at_home = {
        key for key, value in clients["joao"].days.items() if value == 0
    }

    with open("./data/mkt_campaign.txt", "w") as text_file:
        text_file.write(f"{most_popular_food(clients['maria'].foods)}\n")
        text_file.write(f"{str(data['arnaldo']['foods']['hamburguer'])}\n")
        text_file.write(f"{str(joao_not_order)}\n")
        text_file.write(f"{str(joao_at_home)}\n")
