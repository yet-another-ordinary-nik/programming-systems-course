import unittest
from rational import Rational

class TestRational(unittest.TestCase):

    # Тесты инициализации
    def test_initialization_valid(self):
        r = Rational(3, 4)
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 4)

    def test_initialization_zero_denominator(self):
        with self.assertRaises(ValueError):
            Rational(1, 0)

    def test_initialization_negative_denominator(self):
        r = Rational(3, -4)
        self.assertEqual(r.numerator, -3)
        self.assertEqual(r.denominator, 4)

    def test_initialization_float_conversion(self):
        r = Rational(2.5)
        self.assertEqual(r, Rational(5, 2))

    def test_initialization_non_integer_or_float(self):
        with self.assertRaises(TypeError):
            Rational("3", 2)

    # Тесты упрощения дроби
    def test_simplification(self):
        r = Rational(4, 8)
        self.assertEqual(r.numerator, 1)
        self.assertEqual(r.denominator, 2)

    def test_simplification_negative(self):
        r = Rational(-6, 9)
        self.assertEqual(r.numerator, -2)
        self.assertEqual(r.denominator, 3)

    def test_zero_numerator(self):
        r = Rational(0, 5)
        self.assertEqual(r.numerator, 0)
        self.assertEqual(r.denominator, 1)

    # Тесты арифметических операций
    def test_add(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        self.assertEqual(r1 + r2, Rational(5, 6))
        self.assertEqual(r1 + 2, Rational(5, 2))

    def test_sub(self):
        r1 = Rational(3, 4)
        r2 = Rational(1, 4)
        self.assertEqual(r1 - r2, Rational(1, 2))
        self.assertEqual(r1 - 1, Rational(-1, 4))

    def test_mul(self):
        r1 = Rational(2, 3)
        r2 = Rational(3, 4)
        self.assertEqual(r1 * r2, Rational(1, 2))
        self.assertEqual(r1 * 3, Rational(2, 1))

    def test_truediv(self):
        r1 = Rational(3, 4)
        r2 = Rational(1, 2)
        self.assertEqual(r1 / r2, Rational(3, 2))
        self.assertEqual(r1 / 2, Rational(3, 8))

    def test_div_by_zero(self):
        r = Rational(3, 4)
        with self.assertRaises(ZeroDivisionError):
            r / Rational(0, 1)
        with self.assertRaises(ZeroDivisionError):
            r / 0

    # Тесты операций с присваиванием
    def test_iadd(self):
        r = Rational(1, 2)
        r += Rational(1, 3)
        self.assertEqual(r, Rational(5, 6))
        r += 1
        self.assertEqual(r, Rational(11, 6))

    def test_imul(self):
        r = Rational(2, 3)
        r *= Rational(3, 4)
        self.assertEqual(r, Rational(1, 2))
        r *= 4
        self.assertEqual(r, Rational(2, 1))

    # Тесты операций сравнения
    def test_eq(self):
        self.assertEqual(Rational(2, 1), 2)
        self.assertEqual(Rational(4, 2), Rational(2, 1))
        self.assertNotEqual(Rational(3, 4), 1)
        self.assertNotEqual(Rational(3, 4), "invalid")

    def test_equality_with_float(self):
        self.assertEqual(Rational(1, 2), 0.5)
        self.assertEqual(Rational(3, 2), 1.5)

    # Тесты крайних случаев
    def test_large_numbers(self):
        r = Rational(123456, 789012)
        simplified = Rational(10288, 65751)  # GCD(123456, 789012) = 12
        self.assertEqual(r, simplified)

    def test_negative_operations(self):
        r1 = Rational(-3, 4)
        r2 = Rational(2, -5)
        self.assertEqual(r1 + r2, Rational(-23, 20))
        self.assertEqual(r1 * r2, Rational(3, 10))

    # Тесты представления в виде строки
    def test_str(self):
        self.assertEqual(str(Rational(3, 4)), "3/4")
        self.assertEqual(str(Rational(5, 1)), "5/1")

    def test_repr(self):
        self.assertEqual(repr(Rational(3, 4)), "Rational(3, 4)")
        self.assertEqual(repr(Rational(5, 2)), "Rational(5, 2)")

    # Тесты обработки ошибок
    def test_invalid_operations(self):
        r = Rational(3, 4)
        with self.assertRaises(TypeError):
            r + "invalid"
        with self.assertRaises(TypeError):
            r - [1, 2]
        with self.assertRaises(TypeError):
            r * {"a": 1}
        with self.assertRaises(TypeError):
            r / (3.4, 2.1)

if __name__ == '__main__':
    unittest.main()
