import math

class Rational:
    """
    Класс рациональных чисел.
    Рациональное число – число, представимое в виде дроби
    с целым числом в числителе и натуральным числом в знаменателе
    """

    @staticmethod
    def reducedfraction(big_numerator: int, big_denominator: int):
        """
        Статический метод, повышающий удобство работы с вещественными числами, конвертированных в рациональные.
        Возвращает числитель и знаменатель дроби из целых чисел, которая в десятичном представлении совпадает с
        упрощаемым числом до 4 знака после запятой.

        Этот метод призван избавить пользователя от рациональных чисел, представленных
        в виде дробей с очень большими числителями и знаменателями, за счет некоторого уменьшения точности вычислений.

        Пример для наглядности:

            2.3333 = 5254124505271789 / 2251799813685248

            Очевидно, что с таким работать очень тяжело как для пользователя, так и для самой программы.

            Однако мы можем взять дробь с числителем и знаменателем, на порядки меньшими, которая в десятичном представлении
            будет давать, пусть не в точности то число, представление которого мы "упрощаем", но число, достаточно близкое к нему:

            52541 / 22517 = 2.3333925478527333...

        :param big_numerator: Рациональное число, которое нужно "упростить".
        :param big_denominator: Рациональное число, которое нужно "упростить".
        :return: Число типа Rational – "упрощенное" рациональное число.
        """

        if len(str(big_numerator)) > 5:
            reduced_numerator = int(str(big_numerator)[:5])
        else:
            reduced_numerator = big_numerator

        if len(str(big_denominator)) > 5:
            reduced_denominator = int(str(big_denominator)[:5])
        else:
            reduced_denominator = big_denominator

        return reduced_numerator, reduced_denominator

    def __init__(self, numerator, denominator=1):
        """
        Метод инициализации объекта класса Rational (рационального числа).
        Принимает в себя два числа: числитель и знаменатель.
        Может принять в себя объекты классов: int и float;
            В случае float представит вещественное число как дробь из двух целых чисел
            (число типа float будет округлено до 4 знаков после запятой).
        Если это возможно, сокращает дробь.

        :param numerator: Числитель дроби – целое число (int).
        :param denominator: Знаменатель дроби - целое число (int), не равное нулю.
        """

        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        if isinstance(numerator, float):
            f_number = round(numerator/denominator, 4)
            f_number_air = f_number.as_integer_ratio()
            numerator, denominator = Rational.reducedfraction(f_number_air[0], f_number_air[1])

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")

        if denominator < 0:
            numerator, denominator = -numerator, -denominator

        gcd_value = math.gcd(numerator, denominator)
        self.__numerator = numerator // gcd_value
        self.__denominator = denominator // gcd_value

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __add__(self, other):
        """
        Оператор сложения рационального числа с другим рациональным числом или целым числом (int).
        В случае сложения с целым числом предворительно преобразовывет его в рациональное.
        Для типов данных, отличных от Rational и int, операция не определена.

        :param other: Число, с которым происходит сложение.
        :return: Результат сложения двух чисел – сумма двух чисел или ошибка неопределенности операции.
        """

        if isinstance(other, Rational):
            numerator = self.__numerator * other.denominator + other.numerator * self.__denominator
            denominator = self.__denominator * other.denominator
            new_numerator, new_denominator = Rational.reducedfraction(numerator, denominator)
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self + Rational(other)
        else:
            return NotImplemented

    def __sub__(self, other):
        """
        Оператор вычитания из рационального числа другого рационального числа или целого числа (int).
        В случае вычитания целого числа предворительно преобразовывет его в рациональное.
        Для типов данных, отличных от Rational и int, операция не определена.

        :param other: Число, которое вычитается из рационального числа.
        :return: Результат вычитания из одного числа другого – разность двух чисел или ошибка неопределенности операции.
        """

        if isinstance(other, Rational):
            numerator = self.__numerator * other.denominator - other.numerator * self.__denominator
            denominator = self.__denominator * other.denominator
            new_numerator, new_denominator = Rational.reducedfraction(numerator, denominator)
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self - Rational(other)
        else:
            return NotImplemented

    def __mul__(self, other):
        """
        Оператор умножения рационального числа на другое рациональное число или целое число (int).
        В случае умножения на целое число предворительно преобразовывет его в рациональное.
        Для типов данных, отличных от Rational и int, операция не определена.

        :param other: Число, на которое умножается рациональное число.
        :return: Результат умножения двух чисел – произведение двух чисел или ошибка неопределенности операции.
        """

        if isinstance(other, Rational):
            numerator = self.__numerator * other.numerator
            denominator = self.__denominator * other.denominator
            new_numerator, new_denominator = Rational.reducedfraction(numerator, denominator)
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self * Rational(other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        """
        Оператор деления рационального числа на другое рациональное число, отличное от нуля, или целое число (int), отличное от нуля.
        В случае деления на целое число предворительно преобразовывет его в рациональное.
        Для типов данных, отличных от Rational и int, операция не определена.

        :param other: Число, на которое делится рациональное число.
        :return: Результат деления одного числа на другое – частное двух чисел или ошибка неопределенности операции.
        """

        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            numerator = self.__numerator * other.denominator
            denominator = self.__denominator * other.numerator
            new_numerator, new_denominator = Rational.reducedfraction(numerator, denominator)
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self / Rational(other)
        else:
            return NotImplemented

    def __eq__(self, other):
        """
        Оператор проверки равенства рационального числа с другим рациональным числом или целым числом (int).
        В случае целого числа предворительно преобразовывет его в рациональное.
        Для типов данных, отличных от Rational и int, операция не определена.

        :param other: Число, с которым проводится проверка на равенство.
        :return: Результат проверки на равенство – True/False или ошибка неопределенности операции.
        """

        if isinstance(other, Rational):
            return self.__numerator == other.numerator and self.__denominator == other.denominator
        elif isinstance(other, int) or isinstance(other, float):
            return self == Rational(other)
        else:
            return NotImplemented

    def __ne__(self, other):
        """
        Оператор проверки неравенства рационального числа с другим рациональным числом или целым числом (int).
        Оператор, обратный оператору __eq__.
        В случае целого числа предворительно преобразовывет его в рациональное.
        Для типов данных, отличных от Rational и int, операция не определена.

        :param other: Число, с которым проводится проверка на неравенство.
        :return: Результат проверки на неравенство – True/False или ошибка неопределенности операции.
        """

        return not (self == other)

    def __iadd__(self, other):
        """
        Оператор сложения с присваиванием рационального числа с другим рациональным числом или целым числом (int).
        В случае целого числа предворительно преобразовывет его в рациональное.
        Для типов данных, отличных от Rational и int, операция не определена.

        :param other: Число, с которым проводится сложение с присваиванием.
        :return: Результат сложения с присваиванием –
            новый объект класса Rational, равный сумме рационального числа и переданного оператору числа,
            или ошибка неопределенности операции.
        """

        if isinstance(other, Rational):
            numerator = self.__numerator * other.denominator + other.numerator * self.__denominator
            denominator = self.__denominator * other.denominator
            gcd_value = math.gcd(numerator, denominator)
            numerator //= gcd_value
            denominator //= gcd_value
            new_numerator, new_denominator = Rational.reducedfraction(numerator, denominator)
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, int) or isinstance(other, float):
            return self.__iadd__(Rational(other))
        else:
            return NotImplemented

    def __isub__(self, other):
        """
        Оператор вычитания с присваиванием из рационального числа другого рационального числа или целого числа (int).
        В случае целого числа предворительно преобразовывет его в рациональное.
        Для типов данных, отличных от Rational и int, операция не определена.

        :param other: Число, с которым проводится вычитание с присваиванием.
        :return: Результат вычитания с присваиванием –
            новый объект класса Rational, равный разности рационального числа и переданного оператору числа,
            или ошибка неопределенности операции.
        """

        if isinstance(other, Rational):
            numerator = self.__numerator * other.denominator - other.numerator * self.__denominator
            denominator = self.__denominator * other.denominator
            gcd_value = math.gcd(numerator, denominator)
            numerator //= gcd_value
            denominator //= gcd_value
            new_numerator, new_denominator = Rational.reducedfraction(numerator, denominator)
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, int)  or isinstance(other, float):
            return self.__isub__(Rational(other))
        else:
            return NotImplemented

    def __imul__(self, other):
        """
        Оператор умножения с присваиванием рационального числа на другое рациональное число или целое число (int).
        В случае целого числа предворительно преобразовывет его в рациональное.
        Для типов данных, отличных от Rational и int, операция не определена.

        :param other: Число, с которым проводится умножение с присваиванием.
        :return: Результат умножения с присваиванием –
            новый объект класса Rational, равный произведению рационального числа и переданного оператору числа,
            или ошибка неопределенности операции.
        """

        if isinstance(other, Rational):
            numerator = self.__numerator * other.numerator
            denominator = self.__denominator * other.denominator
            gcd_value = math.gcd(numerator, denominator)
            numerator //= gcd_value
            denominator //= gcd_value
            new_numerator, new_denominator = Rational.reducedfraction(numerator, denominator)
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, int)  or isinstance(other, float):
            return self.__imul__(Rational(other))
        else:
            return NotImplemented

    def __itruediv__(self, other):
        """
        Оператор деления с присваиванием рационального числа на другое рациональное число или целое число (int).
        В случае целого числа предворительно преобразовывет его в рациональное.
        Для типов данных, отличных от Rational и int, операция не определена.

        :param other: Число, с которым проводится деление с присваиванием.
        :return: Результат деления с присваиванием –
            новый объект класса Rational, равный частному рационального числа и переданного оператору числа,
            или ошибка неопределенности операции.
        """

        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            numerator = self.__numerator * other.denominator
            denominator = self.__denominator * other.numerator
            gcd_value = math.gcd(numerator, denominator)
            numerator //= gcd_value
            denominator //= gcd_value
            new_numerator, new_denominator = Rational.reducedfraction(numerator, denominator)
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, int)  or isinstance(other, float):
            return self.__itruediv__(Rational(other))
        else:
            return NotImplemented

    def __neg__(self):
        """
        Оператор отрицания рационального числа (умножение на -1).

        :return: Результат отрицания – рациональное число противоположного знака.
        """

        self.__numerator = -self.__numerator
        return self

    def __str__(self):
        """
        Оператор удобного представления рационального числа в виде объекта типа str в формате "числитель/знаменатель".

        :return: Объект типа str в формате "числитель/знаменатель".
        """

        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        """
        Оператор формального представления рационального числа в виде объекта типа str в формате "Rational(числитель, знаменатель)".

        :return: Объект типа str в формате "Rational(числитель, знаменатель)".
        """

        return f"Rational({self.__numerator}, {self.__denominator})"

