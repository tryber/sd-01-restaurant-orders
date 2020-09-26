from unittest.mock import patch, mock_open
from src.analyse_log import analyse_log

# Permite que você substitua partes do seu sistema em teste por objetos
# simulados e faça afirmações sobre como eles foram usados.
# Código baseado no PR do Doug
# https://github.com/tryber/sd-01-restaurant-orders/blob/doug-funny-restaurant-orders/tests/test_analyse_log.py
# Implementação não finilizada


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
        "O prato mais pedido por maria: hamburguer \n",
        "A quantidade de vezes que arnaldo pediu hamburguer foi: 0 \n",
        "O(A) joao nunca pediu: {'misto-quente', 'coxinha', 'pizza'} \n",
        "O(A) joao nunca foi na lanchonete no(s) dia(s): {'segunda-feira', 'sabado'}",
    ]

    def test_analyse_log_if_it_is_working_correctly(self):

        open_mock = mock_open(read_data=self.file_content_mock)
        with patch("builtins.open", open_mock, create=True):
            analyse_log()

        for calls in self.result_test:
            open_mock.return_value.write.assert_any_call(calls)
