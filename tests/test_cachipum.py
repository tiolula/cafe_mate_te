from re import A
from unittest import TestCase
import src.juego as juego

# cafe mata mate: POLEMICA!
# mate mata te
# te mata cafe: NO BEBAS TANTO!
class TestDeCachipum(TestCase):

# Arrange
# Act
# Assert

    #ARRANGE
    def test_ejemplo(self):
        a = 1
        b = 2
        esperado = 3
        # ACT
        resultado = juego.sumar(a, b)
        #ASSERT
        self.assertEqual(esperado, resultado)
