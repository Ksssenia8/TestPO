[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Ksssenia8_TestPO&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Ksssenia8_TestPO)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Ksssenia8_TestPO&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Ksssenia8_TestPO)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Ksssenia8_TestPO&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Ksssenia8_TestPO)

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Ksssenia8_TestPO&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Ksssenia8_TestPO)


### Описание тестов для `quadratic_solver`

| **Тест**                   | **Тип теста**       | **Входные данные**                       | **Описание**                                                                 | **Ожидаемый результат**                   |
|----------------------------|---------------------|------------------------------------------|------------------------------------------------------------------------------|-------------------------------------------|
| `test_two_real_roots`       | Позитивный          | `a=1`, `b=-4`, `c=-5`                   | Проверяет случай с двумя действительными корнями (дискриминант положительный) | Возвращает `[5.0, -1.0]`                  |
| `test_one_real_root`        | Позитивный          | `a=2`, `b=-4`, `c=2`                    | Проверяет случай с одним действительным корнем (дискриминант равен нулю)      | Возвращает `[1.0]`                        |
| `test_no_real_roots`        | Позитивный          | `a=2`, `b=-1`, `c=1`                    | Проверяет случай с отрицательным дискриминантом, когда нет действительных корней | Возвращает `["нет корней"]`              |
| `test_linear_equation`      | Негативный          | `a=0`, `b=2`, `c=-4`                    | Проверяет линейное уравнение (a = 0), где есть одно решение                   | Возвращает `[2.0]`                        |
| `test_not_an_equation`      | Негативный          | `a=0`, `b=0`, `c=-4`                    | Проверяет случай, когда это не уравнение (a = 0, b = 0)                      | Возвращает `["не уравнение"]`             |          |

