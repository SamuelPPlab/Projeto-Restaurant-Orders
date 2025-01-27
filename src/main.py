import csv
from pubsub import pub
from inventory_control import InventoryControl
from track_orders import TrackOrders


def print_info(tracker, control):
    print(control.get_available_dishes())
    print(control.get_quantities_to_buy())


def main():
    topic = 'order'
    path = "data/orders_2.csv"

    tracker = TrackOrders()
    control = InventoryControl()
    subs = [tracker.add_new_order, control.add_new_order]

    for sub in subs:
        pub.subscribe(sub, topic)

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for costumer, order, day in csv_reader:
            pub.sendMessage(topic, costumer=costumer, order=order, day=day)

    print_info(tracker, control)


if __name__ == "__main__":
    main()
