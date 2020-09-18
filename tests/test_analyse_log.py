from unittest.mock import patch, mock_open
from unittest import TestCase
from src.analyse_log import analyse_log


class Test_Analyse_Log(TestCase):

    file_content_mock = """maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira"""

    fake_file_path = "file/path/mock"

    def test_analyse_log(self):
        with patch(
            "builtins.open", mock_open(read_data=self.file_content_mock)
        ) as mock_file:
            assert open(self.fake_file_path).read() == self.file_content_mock
            mock_file.assert_called_with(self.fake_file_path)

        expected = "sei lá!"
        self.assertEqual(expected, actual)

    # def __text_file_reader(self):
    #     with patch('builtins.open', mock_open(read_data=self.mock)) as m:
    #         return m.read()

    # def test_What_is_the_most_requested_dish_for_Maria(self):

    #     with patch("builtins.open", mock_open(read_data=self.mock)) as m:
    #         analyse_log("dummy", "dummy")
    #         given = m.reader()
    #         print(given)
    #         expected = True
    #         assert given == expected

    # def test_How_many_times_did_Arnaldo_order_hamburger(self):
    #     pass

    # def test_Which_dishes_João_never_ordered(self):
    #     NotImplemented

    # def test_What_days_has_João_never_been_to_the_cafeteria(self):
    #     NotImplemented
