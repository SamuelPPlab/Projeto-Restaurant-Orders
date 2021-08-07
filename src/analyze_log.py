import csv


def get_data(path):
    if not path.endswith(".csv"):
        raise ValueError("Arquivo inválido")
    file_obj = csv.reader(open(path))
    return list(file_obj)


def get_favorite(data, client):
    dishes = dict()
    for order in data:
        if order[0] == client:
            dishes[order[1]] = dishes.get(order[1], 0) + 1
    return max(dishes, key=dishes.get)


def get_times_ordered(data, client, dish):
    times_ordered = 0
    for order in data:
        if order[0] == client and order[1] == dish:
            times_ordered += 1
    return times_ordered


def get_never_ordered(data, client):
    all_dishes = list()
    client_dishes = list()
    for order in data:
        all_dishes.append(order[1])
        if order[0] == client:
            client_dishes.append(order[1])
    client_dishes.reverse()
    return set(all_dishes).difference(client_dishes)


def get_missing_days(data, client):
    days = list()
    days_present = list()
    for order in data:
        days.append(order[2])
        if order[0] == client:
            days_present.append(order[2])
    days_present.reverse()
    return set(days).difference(days_present)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(
            "No such file or directory: " "'data/orders_1.txt'"
            )
    data = get_data(path_to_file)
    maria_favorite = get_favorite(data, "maria")
    times_ordered = get_times_ordered(data, "arnaldo", "hamburguer")
    never_ordered = get_never_ordered(data, "joao")
    missing_days = get_missing_days(data, "joao")
    with open("data/mkt_campaign.txt", mode="w") as mkt_campaign:
        mkt_campaign.write(
            f"{maria_favorite}\n"
            f"{times_ordered}\n"
            f"{never_ordered}\n"
            f"{missing_days}"
        )


mock = [['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'hamburguer', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira'], ['maria', 'hamburguer', 'terça-feira'], ['joao', 'hamburguer', 'terça-feira'], ['maria', 'pizza', 'terça-feira'], ['maria', 'coxinha', 'segunda-feira'], ['arnaldo', 'misto-quente', 'terça-feira'], ['jose', 'hamburguer', 'sabado'], ['maria', 'hamburguer', 'terça-feira']]
print(get_missing_days(mock, "joao"))
