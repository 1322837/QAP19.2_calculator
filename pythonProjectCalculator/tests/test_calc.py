import pytest

from app.calculator import Calculator


class Testcalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(20, 10) == 200

    def test_division_success(self):
        assert self.calc.division(20, 10) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(20, 10) == 10

    def test_adding_success(self):
        assert self.calc.adding(20, 10) == 30

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    @staticmethod
    def teardown():
        print('Выполнение метода Teardown')
