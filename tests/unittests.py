import unittest

from calculadora import soma


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_varias_entradas(self):
        # subtest
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200),
        )

        for x_y_saida in x_y_saidas:
            # self.assertEqual(soma(*(x_y_saida[:2])), x_y_saida[-1])
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

    # todos testes devem iniciar com test


unittest.main()
