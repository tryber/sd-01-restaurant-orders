# Crie uma suíte de testes para o método analyse_log
# Obtenha, no mínimo, 90% de cobertura

# Código feito com a ajuda do estudante Doug Funny, mais conhecido como Douglas da Programação
from unittest.mock import patch, mock_open
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

    result_test = [
        "hamburguer \n",
        "0",
        {'coxinha', 'hamburguer', 'misto-quente', 'pizza'},
        {'segunda-feira', 'sabado', 'quinta-feira', 'domingo', 'quarta-feira', 'sexta-feira'},
    ]

    def test_analyse_log_if_it_is_working_correctly(self):

        open_mock = mock_open(read_data=self.file_content_mock)
        with patch("builtins.open", open_mock, create=True):
            analyse_log()

        for calls in self.result_test:
            open_mock.return_value.write.assert_any_call(calls)
