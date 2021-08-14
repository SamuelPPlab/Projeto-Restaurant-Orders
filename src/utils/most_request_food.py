def most_request_food(client_requests: list[tuple]):
    most_repeated_foods = dict()
    most_repeated = None

    for food, _ in client_requests:
        if food in most_repeated_foods:
            most_repeated_foods[food] += 1
        else:
            most_repeated_foods[food] = 1

        if (
            not most_repeated
            or most_repeated_foods[most_repeated] < most_repeated_foods[food]
        ):
            most_repeated = food

    return most_repeated
