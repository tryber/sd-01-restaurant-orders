from csv import DictReader
from service import write_file, import_data, greater_value, group_type, cont_specify_item, not_in_arr, show_values, list_plate, list_days


def analyse_log(path_to_file='data/orders_1.csv'):
    data = import_data(path_to_file)
# Qual o prato mais pedido por 'maria'?
    cont_more_plate_maria = greater_value(
        group_type(data, 'maria', 'client'),
        'plate'
        )
    message_1 = f"Qual o prato mais pedido por 'maria'? {cont_more_plate_maria}"
# Quantas vezes 'arnaldo' pediu 'hamburguer'?
    cont_arnaldo_hamburguer = cont_specify_item(
        group_type(data, 'arnaldo', 'client'),
        'plate',
        'hamburguer'
        )
    message_2 = f"Quantas vezes 'arnaldo' pediu 'hamburguer'? {cont_arnaldo_hamburguer}"
# Quais pratos 'joao' nunca pediu?
    show_plate_joao_dont_order = not_in_arr(list_plate, show_values(group_type(data, 'joao', 'client'), 'plate'))
    message_3 = f"Quais pratos 'joao' nunca pediu? {show_plate_joao_dont_order}"
# Quais dias 'joao' nunca foi na lanchonete?
    joao_dont_go = not_in_arr(list_days, show_values(group_type(data, 'joao', 'client'), 'day'))
    message_4 = f"Quais dias 'joao' nunca foi na lanchonete? {joao_dont_go}"
    write_file('data/mkt_campaign.txt', [message_1, message_2, message_3, message_4])


print(analyse_log())
