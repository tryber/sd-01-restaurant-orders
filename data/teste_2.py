import csv


def read_file_csv(file, plate_favorite):
    with open(file) as csv_file:
        filter_person = []
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if row[0] == plate_favorite:
                filter_person.append(row)
    
    return filter_person


def favorite_food(foods, food_choose):
    most_frequent_food = food_choose
    frequency = {'hamburguer': 0, 'pizza': 0, 'coxinha': 0, 'misto-quente': 0}

    for food in foods:
        index_food = food[1]
        frequency[index_food] += 1

    return frequency[food_choose]


def analyse_log(path_to_file, plate_favorite_person, order_person):

    # filter_plate_favorite = read_file_csv(path_to_file, plate_favorite_person)
    filter_quantity_order = read_file_csv(path_to_file, order_person[0])

    food = favorite_food(filter_quantity_order, order_person[1])

    print(food)


analyse_log('orders_1.csv', "maria", ["arnaldo", "misto-quente"])


