from csv import DictReader


def most_frequent_maria(client):
    most_frequent_lunch = client[0]["lunch"]
    frequency = {}
    for lunch in client:
        if lunch["lunch"] not in frequency:
            frequency[lunch["lunch"]] = 1
        else:
            frequency[lunch["lunch"]] += 1

        if frequency[lunch["lunch"]] > frequency[most_frequent_lunch]:
            most_frequent_lunch = lunch["lunch"]
    return most_frequent_lunch


def f_frequency(keys, client, params_map_key):
    frequency = {k: 0 for k in keys}
    for all_days in client:
        if all_days[params_map_key] not in frequency:
            frequency[all_days[params_map_key]] = 1
        else:
            frequency[all_days[params_map_key]] += 1
    return frequency


def cont_frequent_arnaldo_lunch(keys, client, params_map_key):
    frequency = f_frequency(keys, client, params_map_key)
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


def txt_writing(text, file, path="data/mkt_campaign.txt"):
    with open(path, "a") as f:
        f.write(f"{text} {file} \n")
    print("Dados gravado com sucesso")


def array_of_client(array, cliente):
    return list(filter(lambda x: x["name"] == cliente, array))


def reading_the_main_file(path):
    with open(path, "r") as csvfile:
        fieldnames = ["name", "lunch", "weekday"]
        reader = DictReader(csvfile, fieldnames=fieldnames)
        return [row for row in reader]


def analyse_log(path):
    all_clients = reading_the_main_file(path)

    maria = array_of_client(all_clients, "maria")
    arnaldo = array_of_client(all_clients, "arnaldo")
    joao = array_of_client(all_clients, "joao")

    all_lunch = list(set([row["lunch"] for row in all_clients]))

    all_days = list(set([row["weekday"] for row in all_clients]))

    answer = {
        "maria": " • Qual o prato mais pedido por 'Maria'?",
        "arnaldo": " • Quantas vezes 'Arnaldo' pediu 'hamburguer'?",
        "joao_n": " • Quais pratos 'João' nunca pediu?",
        "joao_d": " • Quais dias 'Joao' nunca foi na lanchonete?",
    }

    try:
        txt_writing(
            answer["maria"],
            most_frequent_maria(maria),
        )

        txt_writing(
            answer["arnaldo"],
            cont_frequent_arnaldo_lunch(all_lunch, arnaldo, "lunch"),
        )

        txt_writing(answer["joao_n"], cont_frequent_joao(all_lunch, joao, "lunch"))

        txt_writing(answer["joao_d"], cont_frequent_joao(all_days, joao, "weekday"))

    except ValueError:
        raise


analyse_log("data/orders_1.csv")
