import csv


days = set(
    [
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sabado",
        "domingo",
    ]
)


def get_all_dishes(arr):
    new_set = set()
    for element in arr:
        new_set.add(element[1])
    return new_set


def days_joao_was_not_the_cafeteria(arr):
    new_set = set()
    for element in arr:
        if element[0] == "joao":
            new_set.add(element[2])
    return days.difference(new_set)


def dishes_joao_never_eated(arr):
    all_dishes = get_all_dishes(arr)
    dishes_joao_asked = set()
    for elements in arr:
        if elements[0] == "joao":
            dishes_joao_asked.add(elements[1])
    return all_dishes.difference(dishes_joao_asked)


def get_dishes_maria(arr):
    new_dict = {}
    most_frequent = 0
    food = ""
    for elements in arr:
        if elements[0] == "maria":
            if elements[1] in new_dict:
                new_dict[elements[1]] += 1
            else:
                new_dict[elements[1]] = 1
            if new_dict[elements[1]] > most_frequent:
                most_frequent = new_dict[elements[1]]
                food = elements[1]
    return food


def number_times_arnold_eats_hamburguer(arr):
    new_dict = {}
    most_frequent = 0
    for elements in arr:
        if elements[0] == "arnaldo" and elements[1] == "hamburguer":
            if elements[1] in new_dict:
                new_dict[elements[1]] += 1
            else:
                new_dict[elements[1]] = 1
            if new_dict[elements[1]] > most_frequent:
                most_frequent = new_dict[elements[1]]
    return most_frequent


def get_csv_data(path_to_file):
    new_data = []
    with open(path_to_file, "r", encoding="utf-8-sig") as csv_file:
        readCSV = csv.reader(csv_file, delimiter=",")
        header, *data = readCSV
        for values in data:
            new_data.append(values)
    return data


def analyse_log(path_to_file="data/orders_1.csv"):
    data = get_csv_data(path_to_file)
    first_answer = get_dishes_maria(data)
    second_answer = number_times_arnold_eats_hamburguer(data)
    test = dishes_joao_never_eated(data)
    four = days_joao_was_not_the_cafeteria(data)

    print(first_answer, second_answer, test, four)


analyse_log()
