[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Ksssenia8_TestPO&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Ksssenia8_TestPO)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Ksssenia8_TestPO&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Ksssenia8_TestPO)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Ksssenia8_TestPO&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Ksssenia8_TestPO)

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Ksssenia8_TestPO&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Ksssenia8_TestPO)


### Описание тестов для `quadratic_solver`

| **Тест**                   | **Тип теста**       | **Описание**                                                                 | **Ожидаемый результат**                   |
|----------------------------|---------------------|------------------------------------------------------------------------------|-------------------------------------------|
| `test_two_real_roots`       | Позитивный      | Проверяет случай с двумя действительными корнями (дискриминант положительный) | Возвращает два корня                      |
| `test_one_real_root`        | Позитивный      | Проверяет случай с одним действительным корнем (дискриминант равен нулю)      | Возвращает один корень                    |
| `test_no_real_roots`        | Позитивный      | Проверяет случай с отрицательным дискриминантом, когда нет действительных корней | Возвращает сообщение "нет корней"        |
| `test_linear_equation`      | Позитивный      | Проверяет линейное уравнение (a = 0), где есть одно решение                   | Возвращает один корень                    |
| `test_not_an_equation`      | негативный      | Проверяет случай, когда это не уравнение (a = 0, b = 0)                      | Возвращает сообщение "не уравнение"       |
| `test_invalid_argument_types` | негативный         | Проверяет передачу аргументов с некорректными типами (например, строки)    | Вызывает ошибку `TypeError`               |
| `test_missing_arguments`    | Негативный         | Проверяет вызов функции с недостаточным числом аргументов                     | Вызывает ошибку `TypeError`               |
| `test_extra_arguments`      | Негативный         | Проверяет вызов функции с лишними аргументами                                | Вызывает ошибку `TypeError`               |

