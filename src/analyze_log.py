import csv


# Função para leitura do csv dos pedidos


def csv_reader(path):
    try:
        with open(path) as data:
            result = list(csv.reader(data))
    except NotImplementedError:
        raise ValueError(f"No such file or directory: {path}")
    return result


# Função para obter comida mais pedida
# Utilizando o vídeo "Resumo + Encontrar o nuúmero mais frequente num array" 
# do bloco 37 - Hashmap e Dict


def get_more_request(name, orders):
    count = {}
    # order do indice 0, informação do indice 1 (comida), para iniciar
    result = orders[0][1]
    for order in orders:
        if order[0] == name:
            if order[1] not in count:
                count[order[1]] = 1
            else:
                count[order[1]] += 1
            if count[order[1]] > count[result]:
                result = order[1]
    return result


# Função para obter comida que não foi pedida
# Utilizando o vídeo "Funções básicas" do bloco 37 - Set


def get_never_request(name, orders):
    all_orders = set()
    order_by_name = set()
    for order in orders:
        all_orders.add(order[1])
    for order in orders:
        if order[0] == name:
            order_by_name.add(order[1])
    return all_orders.difference(order_by_name)


# Função para obter quantas vezes foi pedido um lanche


def get_how_many_times_was_request(name, food, orders):
    result = 0
    for order in orders:
        if order[0] == name and order[1] == food:
            result += 1
    return result


# Função para obter os dias em que o cliente não foi a lanchonete
# Utilizando o vídeo "Funções básicas" do bloco 37 - Set


def get_days_when_you_didnt_go_to_the_cafeteria(name, orders):
    all_days = set()
    day_by_name = set()
    for order in orders:
        all_days.add(order[2])
    for order in orders:
        if order[0] == name:
            day_by_name.add(order[2])
    return all_days.difference(day_by_name)


def analyze_log(path_to_file):
    orders = csv_reader(path_to_file)
    more_request = get_more_request("maria", orders)
    many_times = get_how_many_times_was_request(
        "arnaldo", "hamburguer", orders
    )
    never_request = get_never_request("joao", orders)
    days_without = get_days_when_you_didnt_go_to_the_cafeteria("joao", orders)
    with open("data/mkt_campaign.txt", "w") as data:
        data.write(f"{more_request}\n")
        data.write(f"{many_times}\n")
        data.write(f"{never_request}\n")
        data.write(f"{days_without}\n")
