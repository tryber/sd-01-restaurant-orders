# Crie uma suíte de testes para a classe TrackOrders
# Obtenha, no mínimo, 90% de cobertura

# Código feito com a ajuda do estudante Doug Funny, mais conhecido como Douglas da Programação
from src.track_orders import TrackOrders
from unittest.mock import patch, mock_open


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
        received = "pizza"
        assert expected == received

    def test_get_order_frequency_per_costumer_true(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_dish_quantity_per_costumer("arnaldo", 'hamburguer')
        received = 0
        assert expected == received

    def test_get_never_ordered_per_costumer(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_never_ordered_per_costumer("joao")
        received = {'coxinha', 'misto-quente', 'pizza'}
        assert expected == received

    def test_get_busiest_day(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_busiest_day()
        received = "terça-feira"
        assert expected == received

    def test_get_least_busy_day(self):
        self.__reading_the_main_file()
        expected = self.tracker.get_least_busy_day()
        received = "sabado"
        assert expected == received
