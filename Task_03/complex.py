import math
from rational import Rational


class Complex:
    """
    Класс комплексных чисел.
    Комплексное число – число вида z = (a + ib), где
        a – действительная часть (рациональное число)
        b – мнимая часть (рациональное число)
        i – мнимая единица

    Представить такое число можно парой рациональных коэффициентов a и b
    """

    def __init__(self, real, imaginary=0):
        """
        Метод инициализации объекта класса Complex (комплексного числа).
        Принимает в себя два числа: коэффициенты при действительной части и мнимой части

        :param real: Коэффициент при действительной части (рациональное число)
        :param imaginary: Коэффициент при мнимой части (рациональное число)
        """

        if not isinstance(real, Rational):
            real = Rational(real)
        if not isinstance(imaginary, Rational):
            imaginary = Rational(imaginary)
        self.real = real
        self.imaginary = imaginary

    @staticmethod
    def to_complex(other):
        """
        Статический метод представления числа в виде комплексного

        :param other: Число, которое нужно перевести в комплексную форму
        :return: Результат перевода числа в комплексную форму – комплексное число или ошибка неопределенности операции
        """

        if isinstance(other, Complex):
            return other
        else:
            if isinstance(other, Rational):
                return Complex(other, Rational(0))
            else:
                real_part = Rational(other)
                return Complex(real_part, Rational(0))


    def __add__(self, other):
        """
        Оператор сложения комплексного числа с другим числом.
        Переводит переданное число в комплексную форму, и производит операцию сложения двух комплексных чисел.

        :param other: Число, с которым происходит сложение.
        :return: Результат сложения двух чисел – сумма двух комплексных чисел
            или ошибка неопределенности операции при переводе числа в комплексную форму.
        """

        other = Complex.to_complex(other)
        if other is NotImplemented:
            return NotImplemented
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        """
        Оператор вычитания из комплексного числа другого числа.
        Переводит переданное число в комплексную форму, и производит операцию вычитания.

        :param other: Число, которе вычитается из комплексного числа.
        :return: Результат вычитания – разность двух комплексных чисел
            или ошибка неопределенности операции при переводе числа в комплексную форму.
        """

        other = Complex.to_complex(other)
        if other is NotImplemented:
            return NotImplemented
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        """
        Оператор умножения комплексного числа на другое число.
        Переводит переданное число в комплексную форму, и производит операцию сложения двух комплексных чисел.

        :param other: Число, на которое происходит умножение.
        :return: Результат умножения двух чисел – произведение двух комплексных чисел
            или ошибка неопределенности операции при переводе числа в комплексную форму.
        """

        other = Complex.to_complex(other)
        if other is NotImplemented:
            return NotImplemented
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(new_real, new_imaginary)

    def __truediv__(self, other):
        """
        Оператор деления комплексного числа на другое число.
        Переводит переданное число в комплексную форму, и производит операцию сложения двух комплексных чисел.

        :param other: Число, на которое происходит деление.
        :return: Результат деления двух чисел – частное двух комплексных чисел
            или ошибка неопределенности операции при переводе числа в комплексную форму.
        """

        other = Complex.to_complex(other)
        if other is NotImplemented:
            return NotImplemented
        denominator = other.real * other.real + other.imaginary * other.imaginary
        if denominator == Rational(0, 1):
            raise ZeroDivisionError("Cannot divide by zero.")
        new_real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        new_imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(new_real, new_imaginary)

    def __eq__(self, other):
        """
        Оператор проверки равенства комплексного числа с другим числом.
        Переводит переданное число в комплексную форму, и производит операцию сложения двух комплексных чисел.

        :param other: Число, с которым проводится проверка на равенство.
        :return: Результат проверки на равенство – True/False
            или ошибка неопределенности операции при переводе числа в комплексную форму.
        """

        other = Complex.to_complex(other)
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        """
        Оператор проверки неравенства комплексного числа с другим числом.
        Оператор, обратный оператору __eq__.
        Переводит переданное число в комплексную форму, и производит операцию сложения двух комплексных чисел.

        :param other: Число, с которым проводится проверка на неравенство.
        :return: Результат проверки на неравенство – True/False
            или ошибка неопределенности операции при переводе числа в комплексную форму.
        """

        return not (self == other)

    def __iadd__(self, other):
        """
        Оператор сложения с присваиванием комплексного числа с другим числом.
        Переводит переданное число в комплексную форму, и производит операцию сложения двух комплексных чисел.

        :param other: Число, с которым проводится сложение с присваиванием.
        :return: Результат сложения с присваиванием –
            новый объект класса Complex, равный сумме комплексного числа и переданного оператору числа,
            или ошибка неопределенности операции при переводе числа в комплексную форму.
        """

        other = Complex.to_complex(other)
        if other is NotImplemented:
            return NotImplemented
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return Complex(new_real, new_imaginary)

    def __isub__(self, other):
        """
        Оператор вычитания с присваиванием из комплексного числа другого числа.
        Переводит переданное число в комплексную форму, и производит операцию сложения двух комплексных чисел.

        :param other: Число, с которым проводится вычитание с присваиванием.
        :return: Результат вычитания с присваиванием –
            новый объект класса Complex, равный разности комплексного числа и переданного оператору числа,
            или ошибка неопределенности операции при переводе числа в комплексную форму.
        """

        other = Complex.to_complex(other)
        if other is NotImplemented:
            return NotImplemented
        new_real = self.real - other.real
        new_imaginary = self.imaginary - other.imaginary
        return Complex(new_real, new_imaginary)

    def __imul__(self, other):
        """
        Оператор умножения с присваиванием комплексного числа на другое число.
        Переводит переданное число в комплексную форму, и производит операцию сложения двух комплексных чисел.

        :param other: Число, с которым проводится умножение с присваиванием.
        :return: Результат умножения с присваиванием –
            новый объект класса Complex, равный произведению комплексного числа и переданного оператору числа,
            или ошибка неопределенности операции при переводе числа в комплексную форму.
        """

        other = Complex.to_complex(other)
        if other is NotImplemented:
            return NotImplemented
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(new_real, new_imaginary)

    def __itruediv__(self, other):
        """
        Оператор деления с присваиванием комплексного числа на другое число.
        Переводит переданное число в комплексную форму, и производит операцию сложения двух комплексных чисел.

        :param other: Число, с которым проводится деление с присваиванием.
        :return: Результат деления с присваиванием –
            новый объект класса Complex, равный частному комплексного числа и переданного оператору числа,
            или ошибка неопределенности операции при переводе числа в комплексную форму.
        """

        other = Complex.to_complex(other)
        if other is NotImplemented:
            return NotImplemented
        denominator = other.real * other.real + other.imaginary * other.imaginary
        if denominator == Rational(0, 1):
            raise ZeroDivisionError("Cannot divide by zero.")
        new_real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        new_imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(new_real, new_imaginary)

    def __neg__(self):
        """
        Оператор отрицания комплексного числа (умножение на -1).

        :return: Результат отрицания – комплексное число с коэффициентами противоположного знака.
        """

        new_real = -self.real
        new_imaginary = -self.imaginary
        return Complex(new_real, new_imaginary)

    def __abs__(self):
        """
        Оператор взятия модуля комплексного числа.

        :return: Число типа float – модуль комплексного числа.
        """

        real_squared = self.real * self.real
        imaginary_squared = self.imaginary * self.imaginary
        modulus_squared = real_squared + imaginary_squared
        modulus = math.sqrt(float(modulus_squared.numerator) / float(modulus_squared.denominator))
        return modulus

    def arg(self):
        """
        Оператор взятия аргумента комплексного числа.

        :return: Число типа float – аргумент комплексного числа.
        """

        real_float = float(self.real.numerator) / float(self.real.denominator)
        imaginary_float = float(self.imaginary.numerator) / float(self.imaginary.denominator)
        argument = math.atan2(imaginary_float, real_float)
        return argument

    def power(self, n):
        """
        Оператор возведения комплексного числа в натуральную степень

        :param n: Натуральное число (int) – степень, в которую требуется возвести комплексное число
        :return: Результат (приблизительный, округленный до 4 знака после запятой) возведения комплексного числа в натуральную степень
        """

        if not isinstance(n, int) or n < 0:
            raise ValueError("Exponent must be a natural number (non-negative integer)")

        r = abs(self)
        theta = self.arg()

        # Возводим в степень по теореме Муавра
        new_real = r ** n * math.cos(n * theta)
        new_imaginary = r ** n * math.sin(n * theta)

        # Возвращаемся к рациональным коэффициентам действительной и мнимой части
        real_rational = Rational(new_real)  # Приблизительное значение
        imaginary_rational = Rational(new_imaginary)  # Приблизительное значение

        return Complex(real_rational, imaginary_rational)

    def __str__(self):
        """
        Оператор удобного представления комплексного числа в виде объекта типа str
        в формате "(действительная часть) + (мнимая часть)i".

        :return: Объект типа str в формате "(действительная часть) + (мнимая часть)i".
        """

        return f"({self.real}) + ({self.imaginary})i"

    def __repr__(self):
        """
        Оператор формального представления комплексного числа в виде объекта типа str
        в формате "Complex(действительная часть, мнимая часть)".

        :return: Объект типа str в формате "Complex(действительная часть, мнимая часть)".
        """

        return f"Complex(Rational({self.real.numerator}, {self.real.denominator}), Rational({self.imaginary.numerator}, {self.imaginary.denominator}))"

# r = 4
# print(Complex.to_complex(r))
# Example usage:
# r1 = Rational(1, 2)
# r2 = Rational(3, 4)
# c1 = Complex(r1, r2)
# c2 = Complex(Rational(2, 3), Rational(1, 3))
# c3 = Complex(Rational(1,2), Rational(1,4))
#
# print(c1 + c2)  # Output: (7/6) + (13/12)i
# print(c1 - c2)  # Output: (-1/6) + (5/12)i
# print(c1 * c2)  # Output: (1/12) + (2/3)i
# print(c1 / c2)  # Output: (21/20) + (3/5)i
#
# c1 += c2
# print(c1)  # Output: (7/6) + (13/12)i
#
# c1 *= c2
# print(c1)  # Output: (5/12) + (10/9)i
#
# print(c1 == Complex(Rational(5, 12), Rational(10, 9)))  # Output: True
# print(c1 != Complex(Rational(1, 2), Rational(3, 4)))  # Output: True
#
# print(c3.power(3))
