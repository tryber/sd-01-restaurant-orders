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
    list_favorites_foods = []
    plates = ['segunda-feira', 'terça-feira', 'sabado']
    plates_set = set(plates)

    for food in foods:
        list_favorites_foods.append(food[2])

    list_favorites_foods_set = set(list_favorites_foods)
    return plates_set.difference(list_favorites_foods_set)


def analyse_log(path_to_file, plate_favorite_person, order_person, plates_orders_person):

    # filter_plate_favorite = read_file_csv(path_to_file, plate_favorite_person)
    # filter_quantity_order = read_file_csv(path_to_file, order_person[0])
    filter_plates_favorites = read_file_csv(path_to_file, plates_orders_person)

    food = favorite_food(filter_plates_favorites)

    print(food)


analyse_log('orders_1.csv', "maria", ["arnaldo", "misto-quente"], "joao")

# plates = set(['hamburguer', 'pizza', 'coxinha', 'misto-quente', 'hamburguer'])
# panela = set(['hamburguer', 'pizza'])
# print(plates.difference(panela))
