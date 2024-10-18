import unittest
from main import solve_quadratic_equation  # Импортируем функцию для тестирования


class TestQuadraticEquationModule(unittest.TestCase):  # Класс тестов для проверки решения квадратных уравнений
    def test_positive_discr(self):
        # Тест с положительным дискриминантом: должно быть два действительных корня
        self.assertEqual(solve_quadratic_equation(a=1, b=-4, c=-5), [5.0, -1.0])

    def test_zero_discr(self):
        # Тест с нулевым дискриминантом: должен быть один действительный корень
        self.assertEqual(solve_quadratic_equation(a=2, b=-4, c=2), [1.0])

    def test_negative_discr(self):
        # Тест с отрицательным дискриминантом: корней нет
        self.assertEqual(solve_quadratic_equation(a=2, b=-1, c=1), ["нет корней"])

    def test_zero_a(self):
        # Тест, когда a = 0 (линейное уравнение): должен быть один корень
        self.assertEqual(solve_quadratic_equation(a=0, b=2, c=-4), [2.0])

    def test_zero_a_zero_b(self):
        # Тест, когда a = 0 и b = 0 (это не уравнение): должно вернуть "не уравнение"
        self.assertEqual(solve_quadratic_equation(a=0, b=0, c=-4), ["не уравнение"])

    def test_incorrect_arguments_type(self):
        # Тест с некорректным типом аргументов: должен выдать ошибку TypeError
        with self.assertRaises(TypeError):
            solve_quadratic_equation(a="hello", b=2, c=-4)

    def test_less_number_of_arguments(self):
        # Тест, когда передано меньше аргументов, чем нужно: должен выдать ошибку TypeError
        with self.assertRaises(TypeError):
            solve_quadratic_equation(b=2, c=-4)

    def test_more_number_of_arguments(self):
        # Тест с лишним аргументом: должен выдать ошибку TypeError
        with self.assertRaises(TypeError):
            solve_quadratic_equation(a=2, b=2, c=2, dicr=0)


if __name__ == '__main__':
    unittest.main()  # Запуск тестов при выполнении скрипта
