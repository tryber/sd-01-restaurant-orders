import csv


def read_file_csv(file, plate_favorite):
    with open(file) as csv_file:
        filter_person = []
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if row[0] == plate_favorite:
                filter_person.append(row)

    return filter_person


def favorite_food(foods):
    most_frequent_food = foods[0][1]
    frequency = {}

    for food in foods:

        index_food = food[1]

        if index_food not in frequency:
            frequency[index_food] = 1

        else:
            frequency[index_food] += 1

        if frequency[index_food] > frequency[most_frequent_food]:
            most_frequent_food = index_food

    return most_frequent_food


def quantity_orders_a_food(foods, food_choose):
    frequency = {'hamburguer': 0, 'pizza': 0, 'coxinha': 0, 'misto-quente': 0}

    for food in foods:
        index_food = food[1]
        frequency[index_food] += 1

    return frequency[food_choose]


def foods_not_orders(foods):
    list_favorites_foods = []
    plates = ['hamburguer', 'pizza', 'coxinha', 'misto-quente']
    plates_set = set(plates)

    for food in foods:
        list_favorites_foods.append(food[1])

    list_favorites_foods_set = set(list_favorites_foods)
    return plates_set.difference(list_favorites_foods_set)


def absent_days(foods):
    present_days = []
    days = ['segunda-feira', 'terça-feira', 'sabado']
    days_set = set(days)

    for food in foods:
        present_days.append(food[2])

    present_days_set = set(present_days)
    return days_set.difference(present_days_set)


def analyse_log(path_to_file, plate_favorite, order, plates_orders, absent_person):

    filter_plate_favorite = read_file_csv(path_to_file, plate_favorite)
    filter_quantity_order = read_file_csv(path_to_file, order[0])
    filter_plates_favorites = read_file_csv(path_to_file, plates_orders)
    filter_present_days = read_file_csv(path_to_file, absent_person)

    food_more_order = favorite_food(filter_plate_favorite)
    food_order_total = quantity_orders_a_food(filter_quantity_order, order[1])
    plates_not_orders = foods_not_orders(filter_plates_favorites)
    days_not_present = absent_days(filter_present_days)

    print(food_more_order)
    print(food_order_total)
    print(plates_not_orders)
    print(days_not_present)

    with open('mkt_campaign.txt', 'w', newline='') as file:

        file.write(f"O prato mais pedido por {plate_favorite}: {food_more_order}\n")
        file.write(f"A quantidade de vezes que {order[0]} pediu {order[1]} foi: {food_order_total}\n")
        file.write(f"O(A) {plates_orders} nunca pediu: {plates_not_orders}\n")
        file.write(f"O(A) {absent_person} nunca foi na lanchonete no(s) dia(s): {days_not_present}\n")


analyse_log('orders_1.csv', "maria", ["arnaldo", "hamburguer"], "joao", "joao")
