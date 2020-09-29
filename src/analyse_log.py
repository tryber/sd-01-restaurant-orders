from serv.service import Services
# from service import Services

func_services = Services()


def analyse_log(path_to_file='data/orders_1.csv'):
    data = func_services.import_data(path_to_file)

    print(data, 'data')
    cont_more_plate_maria = func_services.greater_value(
        func_services.group_type(data, 'maria', 'client'),
        'plate'
        )
    message_1 = f"Qual o prato mais pedido por 'maria'? {cont_more_plate_maria}"
    cont_arnaldo_hamburguer = func_services.cont_specify_item(
        func_services.group_type(data, 'arnaldo', 'client'),
        'plate',
        'hamburguer'
        )
    message_2 = f"Quantas vezes 'arnaldo' pediu 'hamburguer'? {cont_arnaldo_hamburguer}"
    show_plate_joao_dont_order = func_services.not_in_arr(func_services.list_plate, func_services.show_values(func_services.group_type(data, 'joao', 'client'), 'plate'))
    message_3 = f"{show_plate_joao_dont_order}"
    joao_dont_go = func_services.not_in_arr(func_services.list_days, func_services.show_values(func_services.group_type(data, 'joao', 'client'), 'day'))
    message_4 = f"{joao_dont_go}"
    print(message_4)
    func_services.write_file('data/mkt_campaign.txt', [message_1, message_2, message_3, message_4])


# analyse_log()
