import unittest  # Импортируем модуль для создания тестов
from main import quadratic_solver  # Импортируем тестируемую функцию из основного модуля

class TestQuadraticSolver(unittest.TestCase):
    # Тест на два действительных корня (положительный дискриминант)
    def test_two_real_roots(self):
        self.assertEqual(quadratic_solver(a=1, b=-4, c=-5), [5.0, -1.0])

    # Тест на один действительный корень (нулевой дискриминант)
    def test_one_real_root(self):
        self.assertEqual(quadratic_solver(a=2, b=-4, c=2), [1.0])

    # Тест на отсутствие действительных корней (отрицательный дискриминант)
    def test_no_real_roots(self):
        self.assertEqual(quadratic_solver(a=2, b=-1, c=1), ["нет корней"])

    # Тест для линейного уравнения (a = 0)
    def test_linear_equation(self):
        self.assertEqual(quadratic_solver(a=0, b=2, c=-4), [2.0])

    # Тест для случая, когда это не уравнение (a = 0, b = 0)
    def test_not_an_equation(self):
        self.assertEqual(quadratic_solver(a=0, b=0, c=-4), ["не уравнение"])


# Запуск всех тестов при запуске скрипта
if __name__ == "__main__":
    unittest.main()
