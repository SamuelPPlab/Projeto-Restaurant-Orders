import csv
from track_orders import TrackOrders


def analyze_log(path_to_file):
    OUTPUT_FILE_NAME = "mkt_campaign.txt"
    tracker = TrackOrders()
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for costumer, order, day in csv_reader:
            tracker.add_new_order(costumer, order, day)

    with open(f"./{OUTPUT_FILE_NAME}", "w") as output_file:
        print(
            tracker.get_most_ordered_dish_per_costumer("maria"),
            tracker.get_dish_quantity_per_costumer("arnaldo", "hamburguer"),
            tracker.get_never_ordered_per_costumer("joao"),
            tracker.get_days_never_visited_per_costumer("joao"),
            sep="\n",
            file=output_file,
        )
