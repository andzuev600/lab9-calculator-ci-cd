class Calculator:
    """
    Класс калькулятора с базовой математической логикой и дополнительными функциями
    """

    def add(self, a, b):
        """Сложение двух чисел"""
        return a + b

    def subtract(self, a, b):
        """Вычитание двух чисел"""
        return a - b

    def multiply(self, a, b):
        """Умножение двух чисел"""
        return a * b

    def divide(self, a, b):
        """
        Деление двух чисел
        Вызывает ValueError при делении на ноль
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно!")
        return a / b

    def power(self, base, exponent):
        """Возведение в степень"""
        return base ** exponent

    def is_prime_number(self, n):
        """
        Проверка, является ли число простым
        Простое число - натуральное число больше 1, которое делится только на 1 и на само себя
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factorial(self, n):
        """
        Вычисление факториала числа
        Факториал n! = 1 * 2 * 3 * ... * n
        """
        if n < 0:
            raise ValueError("Факториал определен только для неотрицательных чисел")
        if n == 0 or n == 1:
            return 1

        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def calculate_expression(self, expression):
        """
        Вычисление математического выражения в виде строки
        Поддерживает базовые операции: +, -, *, /
        """
        # Безопасное вычисление выражения - проверяем символы ДО eval
        allowed_chars = set('0123456789+-*/. ()')
        clean_expression = expression.replace(' ', '')

        if not all(c in allowed_chars for c in clean_expression):
            raise ValueError("Выражение содержит недопустимые символы")

        try:
            result = eval(expression)
            return result
        except ZeroDivisionError:
            raise ValueError("Деление на ноль в выражении")
        except:
            raise ValueError("Некорректное математическое выражение")

# Дополнительные функции для тестирования
def is_even_number(n):
    """Проверка, является ли число четным"""
    return n % 2 == 0


def get_discriminant(a, b, c):
    """
    Вычисление дискриминанта квадратного уравнения
    D = b² - 4ac
    """
    return b ** 2 - 4 * a * c