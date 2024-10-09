import pytest
from main import solve_quadratic

def test_two_real_roots():
    # Тест для уравнения с двумя реальными корнями: x^2 - 3x + 2 = 0
    assert solve_quadratic(1, -3, 2) == (2.0, 1.0)

def test_one_real_root():
    # Тест для уравнения с одним реальным корнем: x^2 - 2x + 1 = 0
    assert solve_quadratic(1, -2, 1) == (1.0,)

def test_no_real_roots():
    # Тест для уравнения без реальных корней: x^2 + 1 = 0
    assert solve_quadratic(1, 0, 1) is None

def test_not_a_quadratic_equation():
    # Тест для случая, когда уравнение не является квадратным (a=0): 2x + 1 = 0
    assert solve_quadratic(0, 2, 1) == (-0.5,)

def test_zero_coefficients():
    # Тест для случая, когда все коэффициенты равны нулю: 0x^2 + 0x + 0 = 0
    assert solve_quadratic(0, 0, 0) is None
