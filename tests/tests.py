import unittest
from main import quadratic_solver


class TestQuadraticSolver(unittest.TestCase):
    def test_two_real_roots(self):
        self.assertEqual(quadratic_solver(a=1, b=-4, c=-5), [5.0, -1.0])

    def test_one_real_root(self):
        self.assertEqual(quadratic_solver(a=2, b=-4, c=2), [1.0])

    def test_no_real_roots(self):
        self.assertEqual(quadratic_solver(a=2, b=-1, c=1), ["нет корней"])

    def test_linear_equation(self):
        self.assertEqual(quadratic_solver(a=0, b=2, c=-4), [2.0])

    def test_not_an_equation(self):
        self.assertEqual(quadratic_solver(a=0, b=0, c=-4), ["не уравнение"])

    def test_invalid_argument_types(self):
        with self.assertRaises(TypeError):
            quadratic_solver(a="invalid", b=2, c=-4)

    def test_missing_arguments(self):
        with self.assertRaises(TypeError):
            quadratic_solver(b=2, c=-4)

    def test_extra_arguments(self):
        with self.assertRaises(TypeError):
            quadratic_solver(a=2, b=2, c=2, extra_param=0)


if __name__ == "__main__":
    unittest.main()
