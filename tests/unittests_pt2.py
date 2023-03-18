"""
TDD - Test driven development 

Red
Parte 1 -> crair teste ver falhar

Green
Parte 2 -> Criar código e ver o teste passar

Refactor 
Parte 3 -> melhorar meu código
"""
import unittest


def bacon_com_ovos(n: int):
    assert isinstance(n, int), 'N deve ser int'
    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
# test.py


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos("")

    def test_bacon_com_ovos_retorna_str_se_entrada_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f"'{entrada}' NÃO retornou '{saida}'")


unittest.main(verbosity=2)
