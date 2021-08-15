def quantity_of_products(person, product, list_foods):
    food = {}
    for people in list_foods:
        if people[0] == person and people[1] == product:
            if people[0] not in food:
                food[product] = 1
            else:
                food[product] += 1

    return f"{str(food[product])}\n"
