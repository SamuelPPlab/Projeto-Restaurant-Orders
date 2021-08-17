import csv


def alimenta_data_datapessoas_pratos_e_dia_consumo(
        data, data_maria, data_arnaldo, data_joao,
        conj_pratos, dias_consumo):
    for index in range(len(data)):
        if data[index][0] == 'maria':
            data_maria.append(data[index][1])
            # data_maria.append(data[index][2])
        if data[index][0] == 'arnaldo':
            data_arnaldo.append(data[index][1])
            # data_arnaldo.append(data[index][2])
        if data[index][0] == 'joao':
            data_joao.append(data[index][1])
            data_joao.append(data[index][2])
        conj_pratos.add(data[index][1])
        dias_consumo.add(data[index][2])


def alimenta_dicionario(string_data, screen):
    for word in string_data:
        if word not in screen:
            screen[word] = 1
        else:
            screen[word] += 1


def analyze_log(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()
        data = []
        data_maria = []
        data_arnaldo = []
        data_joao = []
        conj_joao = set()
        conj_pratos = set()
        dias_consumo = set()
        screen_maria = {}
        screen_arnaldo = {}
        screen_joao = {}
        for row in csv_reader:
            data.append((row[0], row[1], row[2]))
        alimenta_data_datapessoas_pratos_e_dia_consumo(
                data, data_maria,
                data_arnaldo, data_joao, conj_pratos, dias_consumo)
        string_data_maria = [''.join(sub_list) for sub_list in data_maria]
        string_data_arnaldo = [''.join(
            sub_list_arnaldo) for sub_list_arnaldo in data_arnaldo]
        string_data_joao = [''.join(
            sub_list_joao) for sub_list_joao in data_joao]
        alimenta_dicionario(string_data_maria, screen_maria)
        alimenta_dicionario(string_data_arnaldo, screen_arnaldo)
        alimenta_dicionario(string_data_joao, screen_joao)
        # resp 1
        sorted_lunch_maria = sorted(
            screen_maria.items(), key=lambda kv: kv[1], reverse=True)
        maria_prato_mais_pedido = sorted_lunch_maria[0][0]

        # resp 2
        sorted_lunch_arnaldo = sorted(
            screen_arnaldo.items(), key=lambda kv: kv[1], reverse=True)
        arnaldo_quantas_vezes_pediu_hamburguer = sorted_lunch_arnaldo[1][1]

        # resp 3
        sorted_lunch_joao = sorted(
            screen_joao.items(), key=lambda kv: kv[1], reverse=True)
        conj_joao.add(sorted_lunch_joao[0][0])
        joao_pratos_nao_consumidos = conj_pratos - conj_joao

        # resp 4
        joao_dia_consumo = set()
        joao_dia_consumo.add(string_data_joao[1])
        joao_dias_de_nao_consumo = dias_consumo - joao_dia_consumo

        with open('data/mkt_campaign.txt', 'w', newline='') as file:
            writer = csv.writer(file, quotechar=' ')
            writer.writerow([maria_prato_mais_pedido])
            writer.writerow([arnaldo_quantas_vezes_pediu_hamburguer])
            writer.writerow([joao_pratos_nao_consumidos])
            writer.writerow([joao_dias_de_nao_consumo])
