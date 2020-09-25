from src.track_orders import TrackOrders
from unittest.mock import patch, mock_open, MagicMock
from csv import DictReader


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

    def test_add_new_order_and_property(self):
        self.__reading_the_main_file()
        assert len(self.tracker._array) == 37

    def test_get_most_ordered_dish_per_costumer(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_most_ordered_dish_per_costumer("maria")
        received = """O prato favorito do/a Maria é o:
pizza"""
        print("#-" * 45)
        print(expected)
        print("#-" * 45)
        assert expected == received

    def test_get_order_frequency_per_costumer_true(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_order_frequency_per_costumer("jose", "hamburguer")
        received = """O/A Jose consumiu:
12 hamburguer no total"""
        assert expected == received

    def test_get_order_frequency_per_costumer_false(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_order_frequency_per_costumer("jose", "arroz")
        received = """O prato não existe!"""
        print("#-" * 45)
        print(expected)
        print("#-" * 45)
        assert expected == received

    def test_get_never_ordered_per_costumer(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_never_ordered_per_costumer("joao")
        received = """Joao nunca pediu:
coxinha, misto-quente e pizza."""
        print("#-" * 45)
        print(expected)
        print("#-" * 45)
        assert expected == received

    def test_get_days_never_visited_per_costumer(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_days_never_visited_per_costumer("arnaldo")
        received = """Arnaldo nunca foi nos dias:
sabado, segunda-feira e terça-feira."""
        print("#-" * 45)
        print(expected)
        print("#-" * 45)
        assert expected == received
