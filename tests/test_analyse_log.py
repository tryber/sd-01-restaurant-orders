from unittest.mock import patch, mock_open, create_autospec, Mock

# from unittest import TestCase
from src.analyse_log import analyse_log


class Test_Analyse_Log:

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

    def test_analyse_log_mocks(self):
        with patch("builtins.open") as mock:
            with open("texto.txt", "w") as f:
                f.write("teste douglas")

            mock.calls

    # def test_when_timeout_is_not_passed(self, mocker):
    #     """when invoked, default timeout should be considered"""
    #     # preparamos nosso teste modificando o método get por um mock
    #     dummy_path = "file/path/mock"
    #     mocked_get = mocker.patch.object(requests, "get", autospec=True)

    #     # invocamos nossa função
    #     analyse_log(dummy_path)

    #     # a asserção é feita verificando se o método foi chamado
    #     # com os parâmetros corretos
    #     # ou seja, verificamos o comportamento do método
    #     mocked_get.assert_called_once_with(dummy_url, timeout=1)

    # def test_when_called_verify_if_status_code_is_ok(self, mocker):
    #     # preparamos nosso teste modificando o método get por um mock
    #     dummy_url = "dummy url"
    #     mocked_get = mocker.patch.object(requests, "get", autospec=True)

    #     # invocamos nossa função
    #     fetch_page_content(dummy_url)

    #     # a asserção é feita verificando se o método raise_for_status
    #     # do retorno do nosso método
    #     # foi invocado somente uma vez
    #     mocked_get.return_value.raise_for_status.assert_called_once()

    # def test_analyse_log_mocks(self):
    #     mock_function = create_autospec(analyse_log, return_value="number one")
    #     given = mock_function(1)
    #     expected = "number one"
    #     assert given == expected

    # with patch(
    #     "builtins.open", mock_open(read_data=self.file_content_mock)
    # ) as mock_file:
    #     assert open(self.fake_file_path).read() == self.file_content_mock
    #     mock_file.assert_called_with(self.fake_file_path)

    # expected = "sei lá!"
    # self.assertEqual(expected, actual)

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
