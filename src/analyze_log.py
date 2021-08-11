from collections import Counter
import csv


def common_order_user(list_orders, user, specific_order=False):
    order_user = [order[1] for order in list_orders if order[0] == user]
    orders_counted = Counter(order_user)

    if specific_order:
        # print(orders_counted)
        return orders_counted[specific_order]

    most_common_order, counter_order = orders_counted.most_common(1)[0]
    return most_common_order, counter_order


def analyze_log(path_to_file):
    with open(path_to_file, mode="r") as file:
        content = csv.reader(file, delimiter=",", quotechar='"')
        list_orders = [row for row in content]
        result = list()

        # Qual o prato mais pedido por 'maria'?
        order_maria = common_order_user(list_orders, "maria")[0]
        result.append(f"{order_maria}\n")

        # Quantas vezes 'arnaldo' pediu 'hamburguer'?
        counter_hamburguer_arnaldo = common_order_user(
            list_orders, "arnaldo", "hamburguer"
        )
        result.append(f"{counter_hamburguer_arnaldo}\n")

        # Quais pratos 'joao' nunca pediu?
        all_menu_orders = set([order[1] for order in list_orders])
        orders_joao = set(
            [order[1] for order in list_orders if order[0] == "joao"]
        )
        difference_orders_joao = all_menu_orders.difference(orders_joao)
        result.append(f"{difference_orders_joao}\n")

        # Quais dias 'joao' nunca foi na lanchonete?
        all_days = set([order[2] for order in list_orders])
        days_joao = set(
            [order[2] for order in list_orders if order[0] == "joao"]
        )
        difference_days_joao = all_days.difference(days_joao)
        result.append(f"{difference_days_joao}\n")

    with open("./data/mkt_campaign.txt", mode="w") as file:
        # print(result)
        file.writelines(result)


if __name__ == "__main__":
    analyze_log("./data/orders_1.csv")
