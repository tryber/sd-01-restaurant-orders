from src.track_orders import TrackOrders
from unittest.mock import patch, mock_open, MagicMock
from csv import DictReader


# Projeto feito com base no PR do Doug Funny
# https://github.com/tryber/sd-01-restaurant-orders/blob/doug-funny-restaurant-orders/tests/test_track_orders.py

class TestTrackOrders(object):

    tracker = TrackOrders()

    file_content_mock = """joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
maria,coxinha,segunda-feira
maria,pizza,terça-feira
maria,pizza,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,pizza,terça-feira
maria,pizza,terça-feira
arnaldo,misto-quente,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
maria,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
jose,hamburguer,sabado
joao,hamburguer,terça-feira
arnaldo,misto-quente,terça-feira
maria,pizza,terça-feira
maria,hamburguer,terça-feira
maria,coxinha,terça-feira
joao,hamburguer,terça-feira
maria,coxinha,segunda-feira
maria,hamburguer,terça-feira
jose,hamburguer,sabado
jose,hamburguer,sabado
maria,misto-quente,terça-feira
maria,coxinha,segunda-feira
maria,coxinha,segunda-feira
maria,pizza,terça-feira
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
maria,pizza,terça-feira"""

    def __reading_the_main_file(self):

        open_mock = mock_open(read_data=self.file_content_mock)
        with patch("builtins.open", open_mock):
            csv_reader = open("dummy").read()
            assert csv_reader == self.file_content_mock
            open_mock.assert_called_with("dummy")
            array = csv_reader.split("\n")
            new_array = []
            for user in array:
                fist_array = user.split(",")
                dict_inter = {
                    "costumer": fist_array[0],
                    "order": fist_array[1],
                    "day": fist_array[2],
                }
                new_array.append(dict_inter)

            for k in new_array:
                costumer, order, day = k.get("costumer"), k.get("order"), k.get("day")
                self.tracker.add_new_order(costumer, order, day)

    def test_get_most_ordered_dish_per_costumer(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_most_ordered_dish_per_costumer("maria")
        received = "Prato favorito do(a) cliente maria: hamburguer"
        print("#-" * 45)
        print(expected)
        print("#-" * 45)
        assert expected == received

    def test_get_order_frequency_per_costumer_true(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_order_frequency_per_costumer("arnaldo", "hamburguer")
        received = "Quantidade de pedidos de hamburguer feito pelo/a cliente arnaldo: 32"
        assert expected == received

    def test_get_never_ordered_per_costumer(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_never_ordered_per_costumer("joao")
        received = """O/A cliente joao pediu todos os pedidos"""
        print("#-" * 45)
        print(expected)
        print("#-" * 45)
        assert expected == received

    def test_get_days_never_visited_per_costumer(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_days_never_visited_per_costumer("joao")
        received = "O/A cliente joao comparece em todos os dias"
        print("#-" * 45)
        print(expected)
        print("#-" * 45)
        assert expected == received

    def test_get_days_most_visited_per_costumer(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_days_most_visited_per_costumer("joao")
        received = "Dia(s) mais visitado(s) pelo(a) cliente joao: {'terça-feira', 'sabado', 'segunda-feira'}"
        print("#-" * 45)
        print(expected)
        print("#-" * 45)
        assert expected == received
