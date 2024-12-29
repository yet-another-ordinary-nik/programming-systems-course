import unittest
from rational import Rational
from complex import Complex
import math

class TestComplex(unittest.TestCase):

    # Тесты инициализации
    def test_initialization_valid(self):
        c = Complex(Rational(1, 2), Rational(3, 4))
        self.assertEqual(c.real, Rational(1, 2))
        self.assertEqual(c.imaginary, Rational(3, 4))

    def test_implicit_conversion(self):
        c1 = Complex(2, 3.5)
        self.assertEqual(c1.real, Rational(2))
        self.assertEqual(c1.imaginary, Rational(7, 2))

        c2 = Complex(Rational(3, 4), 5)
        self.assertEqual(c2.imaginary, Rational(5))

    def test_invalid_type_initialization(self):
        with self.assertRaises(TypeError):
            Complex("1", Rational(2))
        with self.assertRaises(TypeError):
            Complex(Rational(1), [3, 4])

    # Тесты арифметических операций
    def test_add(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        self.assertEqual(c1 + c2, Complex(4, 6))
        self.assertEqual(c1 + 2, Complex(3, 2))
        self.assertEqual(c1 + 3.5, Complex(Rational(9, 2), 2))

    def test_sub(self):
        c1 = Complex(5, 6)
        c2 = Complex(2, 3)
        self.assertEqual(c1 - c2, Complex(3, 3))
        self.assertEqual(c1 - 2, Complex(3, 6))
        self.assertEqual(c1 - 10, Complex(-5, 6))

    def test_mul(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        self.assertEqual(c1 * c2, Complex(-5, 10))
        self.assertEqual(c1 * 2, Complex(2, 4))
        self.assertEqual(c2 * 0.5, Complex(1.5, 2))

    def test_truediv(self):
        c1 = Complex(1, 1)
        c2 = Complex(1, 1)
        self.assertEqual(c1 / c2, Complex(1, 0))
        self.assertEqual(c1 / 2, Complex(0.5, 0.5))
        self.assertEqual(Complex(4, 0) / 2, Complex(2, 0))

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Complex(1, 1) / Complex(0, 0)
        with self.assertRaises(ZeroDivisionError):
            Complex(3, 4) / 0

    # Тесты операций с присваиванием
    def test_iadd(self):
        c = Complex(1, 2)
        c += Complex(3, 4)
        self.assertEqual(c, Complex(4, 6))
        c += 2
        self.assertEqual(c, Complex(6, 6))

    def test_imul(self):
        c = Complex(1, 2)
        c *= Complex(0, 1)
        self.assertEqual(c, Complex(-2, 1))
        c *= 3
        self.assertEqual(c, Complex(-6, 3))

    # Тесты операций сравнения
    def test_eq(self):
        self.assertEqual(Complex(2, 0), 2)
        self.assertEqual(Complex(1.5, 0), Rational(3, 2))
        self.assertNotEqual(Complex(3, 4), 3)
        with self.assertRaises(TypeError):
            Complex(1, 2) == "invalid"

    # Тесты операций взятия модуля и аргумента
    def test_abs(self):
        self.assertAlmostEqual(abs(Complex(3, 4)), 5.0)
        self.assertAlmostEqual(abs(Complex(Rational(3), Rational(4))), 5.0)
        self.assertAlmostEqual(abs(Complex(0, 0)), 0.0)

    def test_arg(self):
        self.assertAlmostEqual(Complex(1, 1).arg(), math.pi/4)
        self.assertAlmostEqual(Complex(-1, 0).arg(), math.pi)
        self.assertAlmostEqual(Complex(0, 5).arg(), math.pi/2)

    # Тесты возведения в натуральную степень
    def test_power(self):
        c = Complex(1, 1)
        c_pow = c.power(3)
        self.assertEqual(c_pow, Complex(-2,2))

        c_zero = Complex(0, 0)
        self.assertEqual(c_zero.power(5), Complex(0, 0))

    def test_invalid_power(self):
        c = Complex(1, 1)
        with self.assertRaises(ValueError):
            c.power(-2)
        with self.assertRaises(ValueError):
            c.power(2.5)

    # Тесты представления в виде строки
    def test_str(self):
        self.assertEqual(str(Complex(1, 2)), "(1/1) + (2/1)i")
        self.assertEqual(str(Complex(Rational(3, 2), 0)), "(3/2) + (0/1)i")

    def test_repr(self):
        self.assertEqual(repr(Complex(1, 2)), "Complex(Rational(1, 1), Rational(2, 1))")

    # Тесты крайних случаев
    def test_zero_imaginary(self):
        c = Complex(5, 0)
        self.assertEqual(c + 3, Complex(8, 0))
        self.assertEqual(c * 2, Complex(10, 0))

    def test_negative_components(self):
        c = Complex(-2, -3)
        self.assertEqual(abs(c), math.sqrt(13))
        self.assertEqual(c.power(2), Complex(-5, 12))

    # Тесты обработки ошибок
    def test_invalid_operations(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c + "invalid"
        with self.assertRaises(TypeError):
            c - {"a": 1}
        with self.assertRaises(TypeError):
            c * [1, 2]
        with self.assertRaises(TypeError):
            c / (3.4, 2.1)

if __name__ == '__main__':
    unittest.main()