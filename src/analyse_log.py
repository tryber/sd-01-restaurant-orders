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


def get_days_joao_was_not_the_cafeteria(arr):
    new_set = set()
    for element in arr:
        if element[0] == "joao":
            new_set.add(element[2])
    return days.difference(new_set)


def get_dishes_joao_never_eated(arr):
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


def get_times_arnold_eats_hamburguer(arr):
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


class SomeThing():
    def get_csv_data(path_to_file):
        new_data = []
        with open(path_to_file, "r", encoding="utf-8-sig") as csv_file:
            readCSV = csv.reader(csv_file, delimiter=",")
            for values in readCSV:
                new_data.append(values)
        return new_data


def save_log_in_file(arr):
    with open("arquivo.txt", "w") as file:
        for line in arr:
            file.write(str(line) + "\n")


def analyse_log(path_to_file="data/orders_1.csv"):
    data = SomeThing.get_csv_data(path_to_file)
    maria_dishes = get_dishes_maria(data)
    times_arnold_eats_hamburguer = get_times_arnold_eats_hamburguer(data)
    dishes_joao_never_eated = get_dishes_joao_never_eated(data)
    days_joao_was_not_the_cafeteria = get_days_joao_was_not_the_cafeteria(data)
    save_log_in_file(
        [
            maria_dishes,
            times_arnold_eats_hamburguer,
            dishes_joao_never_eated,
            days_joao_was_not_the_cafeteria,
        ]
    )


analyse_log()
