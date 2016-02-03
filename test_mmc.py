from unittest import TestCase

from mmc import mmc, escreve_o_mmc


class TestMmc(TestCase):
    
    def test_retorna_lista_vazia(self):
        with self.assertRaises(Exception):
            mmc(0)

    def test_valor_1(self):
        with self.assertRaises(Exception):
            mmc(1)
        
    def test_valor_2(self):
        resultado = mmc(2)
        self.assertEqual([2], resultado)

    def test_valor_3(self):
        resultado = mmc(3)
        self.assertEqual([3], resultado)

    def test_valor_4(self):
        resultado = mmc(4)
        self.assertEqual([2, 2], resultado)

    def test_valor_10(self):
        resultado = mmc(10)
        self.assertEqual([2, 5], resultado)

    def test_valor_13(self):
        resultado = mmc(13)
        self.assertEqual([13], resultado)

    def test_valor_21(self):
        resultado = mmc(21)
        self.assertEqual([3, 7], resultado)

    def test_valor_194(self):
        resultado = mmc(194)
        self.assertEqual([2, 97], resultado)

    def test_valor_198(self):
        resultado = mmc(198)
        self.assertEqual([2, 3, 3, 11], resultado)


class TestEscreveOMmc(TestCase):
    
    def test_retorna_calculo(self):
        resultado = escreve_o_mmc(10)
        self.assertEqual('10 = 2 x 5', resultado)

    def test_retorna_calculo_complexo(self):
        resultado = escreve_o_mmc(198)
        self.assertEqual('198 = 2 x 3 x 3 x 11', resultado)

    def test_retorna_gorfo(self):
        resultado = escreve_o_mmc(1531581681614)
        self.assertEqual('1531581681614 = 2 x 5717 x 133949771', resultado)    
