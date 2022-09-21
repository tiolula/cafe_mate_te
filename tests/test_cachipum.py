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
# Lucero - Lula
#Flor - Lucero
    #ARRANGE
    def test_ejemplo(self):
        a = 1
        b = 2
        esperado = 3
        # ACT
        resultado = juego.sumar(a, b)
        #ASSERT
        self.assertEqual(esperado, resultado)

    def test_cafe_mata_mate(self):
        opcion_del_jugador_a = "cafe"
        opcion_del_jugador_b = "mate"
        esperado = "cafe"
        # ACT
        resultado = juego.ganar(opcion_del_jugador_a, opcion_del_jugador_b)
        #ASSERT
        self.assertEqual(esperado, resultado)

    def test_mate_mata_te(self):
        opcion_del_jugador_a = "mate"
        opcion_del_jugador_b = "te"
        esperado = "mate"
        # ACT
        resultado = juego.ganar(opcion_del_jugador_a, opcion_del_jugador_b)
        #ASSERT
        self.assertEqual(esperado, resultado)

    def test_te_mata_cafe(self):
        opcion_del_jugador_a = "te"
        opcion_del_jugador_b = "cafe"
        esperado = "te"
        # ACT
        resultado = juego.ganar(opcion_del_jugador_a, opcion_del_jugador_b)
        #ASSERT
        self.assertEqual(esperado, resultado)