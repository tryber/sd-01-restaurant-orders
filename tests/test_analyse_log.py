from analyse_log import analyse_log

# Crie uma suíte de testes para o método analyse_log
# Obtenha, no mínimo, 90% de cobertura


class Test_Analyse_Log:
    def __init__(self):
        self.path_orders_1 = "data/orders_1.csv"
        self.path_orders_2 = "data/orders_2.csv"
        self.path_mkt_campaign = "data/mkt_campaign.txt"

    def __text_file_reader(self):
        txt_file = open(self.path_mkt_campaign, "r")
        return txt_file.read()

    def test_What_is_the_most_requested_dish_for_Maria(self):
        given = analyse_log(self.path_orders_1)
        expected = True
        assert given is expected

    def test_How_many_times_did_Arnaldo_order_hamburger(self):
        pass

    def test_Which_dishes_João_never_ordered(self):
        NotImplemented

    def test_What_days_has_João_never_been_to_the_cafeteria(self):
        NotImplemented
