import unittest
from unittest.mock import patch
from io import StringIO
from composite import *

class TestMenu(unittest.TestCase):

    def setUp(self):
        # Crear instancias de elementos individuales
        self.pizza_margarita = Pizza("Margarita", 10.0)
        self.bebida_cola = Bebida("Coca-Cola", 2.0)
        self.entrante_ensalada = Entrante("Ensalada", 5.0)

        # Crear combos predefinidos
        self.combo_1 = Combo("Combo 1")
        self.combo_1.agregar(self.entrante_ensalada)
        self.combo_1.agregar(self.pizza_margarita)
        self.combo_1.agregar(self.bebida_cola)

        self.combo_2 = Combo("Combo 2")
        self.combo_2.agregar(self.entrante_ensalada)
        self.combo_2.agregar(self.pizza_margarita)
        self.combo_2.agregar(self.bebida_cola)

        # Crear Combo Duo predefinido
        self.combo_duo_1 = ComboDuo("Combo Pareja 1")
        self.combo_duo_1.personalizar(self.combo_1, self.combo_2)

    def test_pizza_creation(self):
        self.assertEqual(self.pizza_margarita.nombre, "Margarita")
        self.assertEqual(self.pizza_margarita.precio, 10.0)

    def test_bebida_creation(self):
        self.assertEqual(self.bebida_cola.nombre, "Coca-Cola")
        self.assertEqual(self.bebida_cola.precio, 2.0)

    def test_entrante_creation(self):
        self.assertEqual(self.entrante_ensalada.nombre, "Ensalada")
        self.assertEqual(self.entrante_ensalada.precio, 5.0)

    def test_combo_creation(self):
        self.assertEqual(self.combo_1.nombre, "Combo 1")
        self.assertEqual(len(self.combo_1.elementos), 3)

    def test_combo_pareja_creation(self):
        self.assertEqual(self.combo_duo_1.nombre, "Combo Duo 1")
        self.assertIsNotNone(self.combo_duo_1.combo1)
        self.assertIsNotNone(self.combo_duo_1.combo2)

    @patch("builtins.input", side_effect=["1"])
    def test_solicitar_opcion_valida(self, mock_input):
        opciones = [1, 2, 3]
        eleccion = solicitar_opcion("Elige una opción (1, 2, o 3): ", opciones)
        self.assertEqual(eleccion, 1)

    @patch("builtins.input", side_effect=["4", "3"])
    def test_solicitar_opcion_invalida_then_valida(self, mock_input):
        opciones = [1, 2, 3]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            eleccion = solicitar_opcion("Elige una opción (1, 2, o 3): ", opciones)
            self.assertEqual(eleccion, 3)
            self.assertEqual(mock_stdout.getvalue().strip(), "Opción no válida. Por favor, elige una opción válida.")

    @patch("builtins.input", side_effect=["a", "2"])
    def test_solicitar_opcion_no_entero_then_valida(self, mock_input):
        opciones = [1, 2, 3]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            eleccion = solicitar_opcion("Elige una opción (1, 2, o 3): ", opciones)
            self.assertEqual(eleccion, 2)
            self.assertEqual(mock_stdout.getvalue().strip(), "Error: Ingresa un número entero.")

if __name__ == "__main__":
    unittest.main()