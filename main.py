from math import sqrt


def quadratic_solver(a: float, b: float, c: float) -> list:
    if a == 0:
        return ["не уравнение"] if b == 0 else [-c / b]

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        return [root1, root2]
    elif discriminant == 0:
        return [-b / (2 * a)]
    else:
        return ["нет корней"]


def main():
    result = quadratic_solver(1, -4, -5)
    for index, value in enumerate(result, start=1):
        if isinstance(value, float):
            print(f"x{index} = {value}")
        else:
            print(f"{value}")


if __name__ == "__main__":
    main()
