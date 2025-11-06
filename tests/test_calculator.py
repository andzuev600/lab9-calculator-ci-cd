import pytest
import sys
import os

# Добавляем путь к модулю с калькулятором
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from calculator_class import Calculator, is_even_number, get_discriminant


class TestCalculator:
    """Тесты для класса Calculator"""

    @pytest.fixture
    def calc(self):
        """Фикстура для создания экземпляра калькулятора перед каждым тестом"""
        return Calculator()

    # Тестирование метода add с параметризацией
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),  # положительные числа
        (-2, -3, -5),  # отрицательные числа
        (0, 5, 5),  # ноль + положительное
        (2.5, 3.5, 6.0),  # дробные числа
        (-2.5, 1.5, -1.0),  # дробные с разными знаками
    ])
    def test_add(self, calc, a, b, expected):
        """Тестирование сложения с разными наборами данных"""
        result = calc.add(a, b)
        assert result == expected, f"Ожидалось {expected}, получено {result}"

    # Тестирование метода subtract с параметризацией
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),
        (3, 5, -2),
        (0, 5, -5),
        (2.5, 1.5, 1.0),
        (-2, -3, 1),
    ])
    def test_subtract(self, calc, a, b, expected):
        """Тестирование вычитания"""
        result = calc.subtract(a, b)
        assert result == expected

    # Тестирование метода multiply с параметризацией
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (-2, 3, -6),
        (2, -3, -6),
        (-2, -3, 6),
        (0, 5, 0),
        (2.5, 4, 10.0),
    ])
    def test_multiply(self, calc, a, b, expected):
        """Тестирование умножения"""
        result = calc.multiply(a, b)
        assert result == expected

    # Тестирование метода divide с параметризацией
    @pytest.mark.parametrize("a, b, expected", [
        (6, 3, 2),
        (5, 2, 2.5),
        (-6, 3, -2),
        (0, 5, 0),
        (2.5, 0.5, 5.0),
    ])
    def test_divide_normal_cases(self, calc, a, b, expected):
        """Тестирование деления в нормальных случаях"""
        result = calc.divide(a, b)
        assert result == expected

    def test_divide_by_zero(self, calc):
        """Тестирование исключения при делении на ноль"""
        with pytest.raises(ValueError, match="Деление на ноль невозможно!"):
            calc.divide(5, 0)

    # Тестирование метода power с параметризацией
    @pytest.mark.parametrize("base, exponent, expected", [
        (2, 3, 8),
        (5, 0, 1),
        (2, -1, 0.5),
        (4, 0.5, 2.0),
    ])
    def test_power(self, calc, base, exponent, expected):
        """Тестирование возведения в степень"""
        result = calc.power(base, exponent)
        assert result == expected

    # Тестирование метода is_prime_number с параметризацией
    @pytest.mark.parametrize("number, expected", [
        (2, True),  # наименьшее простое
        (3, True),
        (17, True),
        (4, False),  # составное
        (1, False),  # не простое по определению
        (0, False),  # не простое
        (-5, False),  # отрицательное
        (97, True),  # большое простое
        (100, False),  # составное
    ])
    def test_is_prime_number(self, calc, number, expected):
        """Тестирование проверки простых чисел"""
        result = calc.is_prime_number(number)
        assert result == expected

    # Тестирование метода factorial с параметризацией
    @pytest.mark.parametrize("n, expected", [
        (0, 1),  # 0! = 1
        (1, 1),  # 1! = 1
        (5, 120),  # 5! = 120
        (3, 6),  # 3! = 6
    ])
    def test_factorial_normal_cases(self, calc, n, expected):
        """Тестирование факториала в нормальных случаях"""
        result = calc.factorial(n)
        assert result == expected

    def test_factorial_negative(self, calc):
        """Тестирование исключения для отрицательного факториала"""
        with pytest.raises(ValueError, match="Факториал определен только для неотрицательных чисел"):
            calc.factorial(-5)

    # Тестирование метода calculate_expression
    @pytest.mark.parametrize("expression, expected", [
        ("2 + 3", 5),
        ("10 - 4", 6),
        ("3 * 4", 12),
        ("15 / 3", 5),
        ("(2 + 3) * 4", 20),
    ])
    def test_calculate_expression_valid(self, calc, expression, expected):
        """Тестирование вычисления валидных выражений"""
        result = calc.calculate_expression(expression)
        assert result == expected

    def test_calculate_expression_division_by_zero(self, calc):
        """Тестирование деления на ноль в выражении"""
        with pytest.raises(ValueError, match="Деление на ноль в выражении"):
            calc.calculate_expression("5 / 0")

    def test_calculate_expression_invalid_chars(self, calc):
        """Тестирование выражения с недопустимыми символами"""
        with pytest.raises(ValueError):
            calc.calculate_expression("2 + abc")

    def test_calculate_expression_truly_invalid_chars(self, calc):
        """Тестирование выражения с действительно недопустимыми символами"""
        with pytest.raises(ValueError, match="Выражение содержит недопустимые символы"):
            calc.calculate_expression("2 @ 3")


class TestAdditionalFunctions:
    """Тесты для дополнительных функций"""

    @pytest.mark.parametrize("number, expected", [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-7, False),
        (100, True),
    ])
    def test_is_even_number(self, number, expected):
        """Тестирование проверки четности чисел"""
        result = is_even_number(number)
        assert result == expected

    @pytest.mark.parametrize("a, b, c, expected", [
        (1, -3, 2, 1),
        (1, -2, 1, 0),
        (1, 1, 1, -3),
        (2, 4, 2, 0),
        (1, 5, 6, 1),
    ])
    def test_get_discriminant(self, a, b, c, expected):
        """Тестирование вычисления дискриминанта"""
        result = get_discriminant(a, b, c)
        assert result == expected


class TestEdgeCases:
    """Тесты граничных случаев"""

    @pytest.fixture
    def calc(self):
        return Calculator()

    def test_large_numbers(self, calc):
        """Тестирование работы с большими числами"""
        result = calc.add(10 ** 10, 10 ** 10)
        assert result == 2 * 10 ** 10

    def test_floating_point_precision(self, calc):
        """Тестирование точности вычислений с плавающей точкой"""
        result = calc.add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10

    def test_very_small_numbers(self, calc):
        """Тестирование работы с очень маленькими числами"""
        result = calc.multiply(0.0001, 0.0001)
        assert result == 1e-8