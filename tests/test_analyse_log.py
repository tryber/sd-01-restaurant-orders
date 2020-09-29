from unittest.mock import patch, mock_open
from src.analyse_log import analyse_log
from serv.service import Services


# Codigo copiado do projeto do DOug https://github.com/tryber/sd-01-restaurant-orders/pull/2/files


class Test_Analyse_Log:

    file_content_mock = [
        {'client': 'maria', 'plate': 'hamburguer', 'day': 'terça-feira'},
        {'client': 'joao', 'plate': 'hamburguer', 'day': 'terça-feira'},
        {'client': 'maria', 'plate': 'pizza', 'day': 'segunda-feira'},
        {'client': 'maria', 'plate': 'coxinha', 'day': 'terça-feira'},
        {'client': 'arnaldo', 'plate': 'misto-quente', 'day': 'terça-feira'},
        {'client': 'jose', 'plate': 'hamburguer', 'day': 'sabado'},
        {'client': 'maria', 'plate': 'hamburguer', 'day': 'terça-feira'},
        {'client': 'maria', 'plate': 'hamburguer', 'day': 'terça-feira'},
        {'client': 'joao', 'plate': 'hamburguer', 'day': 'terça-feira'},
        {'client': 'maria', 'plate': 'pizza', 'day': 'terça-feira'},
        {'client': 'maria', 'plate': 'coxinha', 'day': 'segunda-feira'},
        {'client': 'arnaldo', 'plate': 'misto-quente', 'day': 'terça-feira'}]

    result_test = [
        "Qual o prato mais pedido por 'maria'? ['hamburguer', 3]\n",
        "Quantas vezes 'arnaldo' pediu 'hamburguer'? ['hamburguer', 0]\n",
        "{'pizza', 'coxinha', 'misto-quente'}\n",
        "{sabado, segunda-feira, quarta-feira, quinta-feira, domingo, sexta-feira}\n",
    ]
    
    def test_analyse_log_if_it_is_working_correctly2(self):
        with patch.object(Services, "import_data", return_value=self.file_content_mock):
            open_mock = mock_open(read_data=self.file_content_mock)
            with patch("builtins.open", open_mock, create=True):
                analyse_log()

            for calls in self.result_test:
                open_mock.return_value.write.assert_any_call(calls)


