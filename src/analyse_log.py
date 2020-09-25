from csv import DictReader


def f_frequency(keys, client, params_map_key):
    frequency = {k: 0 for k in sorted(keys)}
    for all_days in client:
        frequency[all_days[params_map_key]] += 1
    return frequency


def most_frequent_maria(client):
    most_frequent_lunch = client[0]["lunch"]
    frequency = {}
    for lunch in client:
        if lunch["lunch"] not in frequency:
            frequency[lunch["lunch"]] = 1
        else:
            frequency[lunch["lunch"]] += 1

        # if frequency[lunch["lunch"]] > frequency[most_frequent_lunch]:
        #     most_frequent_lunch = lunch["lunch"]
    return most_frequent_lunch


def cont_frequent_arnaldo_lunch(keys, client):
    frequency = f_frequency(keys, client, "lunch")
    answer = ""
    for k, v in frequency.items():
        if k == "hamburguer":
            answer += f"foram {v} {k}, "
    return answer


def cont_frequent_joao(keys, client, params_map_key):
    frequency = f_frequency(keys, client, params_map_key)
    answer = " "
    for k, v in frequency.items():
        if v == 0:
            answer += f"{k}, "
    return answer


def txt_writing(text, answer, path):
    with open(path, "a") as f:
        f.write(f"{text} {answer} \n")

    return f.close()


def array_of_client(array, cliente):
    return list(filter(lambda x: x["name"] == cliente, array))


def reading_the_main_file(path):
    with open(path, "r") as csvfile:
        fieldnames = ["name", "lunch", "weekday"]
        reader = DictReader(csvfile, fieldnames=fieldnames)
        return [row for row in reader]


def filter_all(key, clients):
    return list(set([row[key] for row in clients]))


def format_answer_per_costumer(
    person,
    path_reading,
    path_write,
):

    all_clients = reading_the_main_file(path_reading)

    list_client = array_of_client(all_clients, person)

    all_lunch = filter_all("lunch", all_clients)

    all_days = filter_all("weekday", all_clients)

    def maria():
        return txt_writing(
            " • Qual o prato mais pedido por 'Maria'?",
            most_frequent_maria(list_client),
            path_write,
        )

    def arnaldo():
        return txt_writing(
            " • Quantas vezes 'Arnaldo' pediu 'hamburguer'?",
            cont_frequent_arnaldo_lunch(all_lunch, list_client),
            path_write,
        )

    def joao_never_ate():
        return txt_writing(
            " • Quais pratos 'João' nunca pediu?",
            cont_frequent_joao(all_lunch, list_client, "lunch"),
            path_write,
        )

    def joao_frequency_of_days():
        return txt_writing(
            " • Quais dias 'João' nunca foi na lanchonete?",
            cont_frequent_joao(all_days, list_client, "weekday"),
            path_write,
        )

    switcher = {
        "maria": maria,
        "arnaldo": arnaldo,
        "joao_never_ate": joao_never_ate,
        "joao_frequency_of_days": joao_frequency_of_days,
    }

    return switcher.get(person, lambda: "Cliente não cadastrado")()


def analyse_log(path="data/mkt_campaign.txt"):

    clients = ["maria", "arnaldo", "joao_never_ate", "joao_frequency_of_days"]

    for client in clients:
        try:
            format_answer_per_costumer(
                client,
                "data/orders_1.csv",
                path,
            )
        except ValueError:
            raise
    return None
