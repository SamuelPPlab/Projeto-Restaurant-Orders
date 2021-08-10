from src.csv_importer import CsvImporter
from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    data = CsvImporter.import_data(path_to_file)
    orders = TrackOrders()

    for item in data:
        costumer = item[0]
        order = item[1]
        day = item[2]
        orders.add_new_order(costumer, order, day)

    dish_quantity_per_arnaldo = orders.get_dish_quantity_per_costumer(
        "arnaldo", "hamburguer"
    )
    with open("./data/mkt_campaign.txt", "w") as text_file:
        text_file.write(
            f"{orders.get_most_ordered_dish_per_costumer('maria')}\n"
        )
        text_file.write(f"{dish_quantity_per_arnaldo}\n")
        text_file.write(f"{orders.get_never_ordered_per_costumer('joao')}\n")
        text_file.write(
            f"{orders.get_days_never_visited_per_costumer('joao')}\n"
        )


analyze_log("./data/orders_1.csv")
