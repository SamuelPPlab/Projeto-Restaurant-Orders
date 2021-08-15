def main():
    topic = 'order'
    path = "data/orders_1.csv"

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
