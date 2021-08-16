import csv

HAMBURGUER = 'hamburguer'
GRAVAR_AQUI = "data/mkt_campaign.txt"

def work_this_csv(path_to_file):
    with open(path_to_file) as this_file:
        keys = ["person", "dish", "day"]
        worked = csv.DictReader(this_file, fieldnames=keys)
        output = []
        for row in worked:
            output.append(row)
        return output


def find_marias_favorite_dish(orders_file):
    marias_orders = []
    for order in orders_file:
        if order['person'] == 'maria':
            marias_orders.append(order['dish'])
    count = 0
    dish = ''
    for order in marias_orders:
        this_dish = marias_orders.count(order)
        if(this_dish > count):
            count = this_dish
            dish = order
    return dish


def os_burge_do_arnaldo(orders_file):
    arnaldos_orders = []
    for row in orders_file:
        if row['person'] == 'arnaldo':
            arnaldos_orders.append(row['dish'])
    return arnaldos_orders.count(HAMBURGUER)


def o_que_o_fresco_do_joao_nao_come(ordes_file):
    all_dishes  = []
    joaos_dishes = []
    joaos_no_go = []
    for order in ordes_file:
        if order['person'] == 'joao' and order['dish'] not in joaos_dishes:
            joaos_dishes.append(order['dish'])
        if(order['dish'] not in all_dishes):
            all_dishes.append(order['dish'])
    for dish in all_dishes:
        if dish not in joaos_dishes:
            joaos_no_go.append(dish)
    return {joaos_no_go[2], joaos_no_go[1], joaos_no_go[0]}


def esses_dias_o_joao_nao(orders_file):
    all_days= []
    joao_days = []
    for order in orders_file:
        if order['person'] == 'joao' and order['day'] not in joao_days:
            joao_days.append(order['day'])
        if order['day'] not in all_days:
            all_days.append(order['day'])
    nao_joao = []
    for day in all_days:
        if day not in joao_days:
            nao_joao.append(day)
    return {nao_joao[1], nao_joao[0]}


def analyze_log(path_to_file):
    orders = work_this_csv(path_to_file)

    favorite_dish = find_marias_favorite_dish(orders)
    arnaldos_burguers_count = os_burge_do_arnaldo(orders)
    arnaldos_no_go = o_que_o_fresco_do_joao_nao_come(orders)
    o_jao_nao = esses_dias_o_joao_nao(orders)

    output = [
    f"{favorite_dish}\n",
    f"{arnaldos_burguers_count}\n",
    f"{arnaldos_no_go}\n",
    f"{o_jao_nao}\n",
    ]
    with open(GRAVAR_AQUI, "w") as here:
        here.writelines(output)
