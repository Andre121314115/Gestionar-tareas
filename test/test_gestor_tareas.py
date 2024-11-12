import unittest
from gestor_tareas import GestorTareas, Tarea

class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        """ Configuración previa para cada test """
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        """ Verificar que se puede agregar una tarea correctamente """
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0].titulo, "Tarea 1")
        self.assertEqual(self.gestor.tareas[0].descripcion, "Descripción de la tarea 1")
        self.assertFalse(self.gestor.tareas[0].completada)

    def test_agregar_tarea_sin_titulo(self):
        """ Verificar que no se puede agregar una tarea sin título """
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("", "Descripción sin título")

    def test_marcar_completada(self):
        """ Verificar que se puede marcar una tarea como completada """
        self.gestor.agregar_tarea("Tarea 2", "Descripción de la tarea 2")
        self.gestor.marcar_completada(0)
        self.assertTrue(self.gestor.tareas[0].completada)

    def test_eliminar_tarea(self):
        """ Verificar que se puede eliminar una tarea correctamente """
        self.gestor.agregar_tarea("Tarea 3", "Descripción de la tarea 3")
        self.gestor.eliminar_tarea(0)
        self.assertEqual(len(self.gestor.tareas), 0)

    def test_eliminar_tarea_fuera_de_rango(self):
        """ Verificar que no se puede eliminar una tarea que no existe """
        with self.assertRaises(IndexError):
            self.gestor.eliminar_tarea(5)  # Índice fuera de rango

    def test_marcar_completada_fuera_de_rango(self):
        """ Verificar que no se puede marcar como completada una tarea que no existe """
        with self.assertRaises(IndexError):
            self.gestor.marcar_completada(5)  # Índice fuera de rango


# Ejecución de los tests
if __name__ == '__main__':
    unittest.main()
