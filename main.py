from math import sqrt

# Функция для решения квадратного уравнения
def quadratic_solver(a: float, b: float, c: float) -> list:
    # Проверка случая, когда a равно 0: это не квадратное уравнение
    if a == 0:
        # Если также b равно 0, это не уравнение; иначе это линейное уравнение
        return ["не уравнение"] if b == 0 else [-c / b]

    # Вычисление дискриминанта
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        # Если дискриминант положителен, уравнение имеет два действительных корня
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        return [root1, root2]
    elif discriminant == 0:
        # Если дискриминант равен нулю, уравнение имеет один корень
        return [-b / (2 * a)]
    else:
        # Если дискриминант отрицателен, корней нет
        return ["нет корней"]

# Основная функция, выполняющая программу
def main():
    # Пример использования функции: решаем уравнение с коэффициентами 1, -4, -5
    result = quadratic_solver(1, -4, -5)
    # Проходим по результатам, выводим корни или сообщение, если корней нет
    for index, value in enumerate(result, start=1):
        if isinstance(value, float):
            print(f"x{index} = {value}")  # Выводим корень, если это число
        else:
            print(f"{value}")  # Выводим сообщение, если корней нет

# Выполняем основную функцию при запуске скрипта
if __name__ == "__main__":
    main()
